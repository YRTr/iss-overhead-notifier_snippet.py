This project checks if the International Space Station (ISS) is overhead based on your location and sends an email notification if it's visible in the night sky. The program integrates APIs and uses various Python libraries to perform geolocation checks, time calculations, and automated email notifications.

#### Libraries and Modules Used

- **Requests**: Used to interact with the [Open Notify API](http://open-notify.org/) to get the current position of the ISS and a weather API to check local conditions.
- **Datetime**: This module helps manage and calculate local sunrise and sunset times to determine if it's nighttime.
- **SMTP (Simple Mail Transfer Protocol)**: Configured to send an email notification if the ISS is overhead and visibility conditions are favorable.
- **JSON**: Parses the data from API responses for easy access to coordinates and ISS positioning information.
  
#### Project Overview

1. **Fetches ISS Location**: The program uses the Open Notify API to retrieve real-time ISS coordinates.
2. **Determines Nighttime Conditions**: Retrieves sunrise and sunset times for your location to ensure notifications are only sent at night.
3. **Automated Notifications**: An email alert is sent via the SMTP library, letting you know when the ISS is visible.


