import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import pytz
import time
import smtplib

geolocator = Nominatim(user_agent="my_loc")
location = geolocator.geocode("New York")

MY_LAT = location.latitude
MY_LNG = location.longitude
MY_EMAIL = "yrtshaan2422@gmail.com"
MY_PW = "cwqs xyxu hblf bpzs"


def is_night():
    payload = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=payload)
    response.raise_for_status()
    data = response.json()
    print(data)

    timestamp1 = data["results"]['sunrise']
    timestamp2 = data["results"]['sunset']
    # convert from UTC to local time
    dt1 = datetime.fromisoformat(timestamp1.replace("Z", "+00:00")).replace(tzinfo=None)
    dt2 = datetime.fromisoformat(timestamp2.replace("Z", "+00:00")).replace(tzinfo=None)

    utc = pytz.utc
    local_tz = pytz.timezone('America/New_York')
    dt1 = utc.localize(dt1).astimezone(local_tz)
    dt2 = utc.localize(dt2).astimezone(local_tz)

    sunrise_time = dt1.time()
    sunset_time = dt2.time()

    time_now: time = datetime.now(local_tz).time()
    print(dt1, dt2)
    print(sunrise_time, sunset_time, time_now)
    if time_now <= sunrise_time or time_now >= sunset_time:
        return True


def is_iss_on_top():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    resp = response.json()
    lat = resp['iss_position']['latitude']
    lng = resp['iss_position']['longitude']
    if abs(MY_LAT - lat) <= 10 or abs(MY_LNG - lng) <= 10:
        return True


while True:
    time.sleep(60)
    if is_night and is_iss_on_top:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Look! ISS is right above you in the sky!"
            )
