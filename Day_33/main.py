import smtplib
import requests
from datetime import datetime

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    my_longitude = -33.938803
    my_latitude = 18.469391

    lng = longitude - my_longitude
    lat = latitude - my_latitude

    if -5 <= lng <= 5 and -5 <= lat <= 5:
        return True

def is_night():
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "formated": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"])
    sunset = int(response.json()["results"]["sunset"])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    MY_EMAIL = input("Enter your gmail.")
    MY_PASSWORD = input("Enter your password.")
    connection = smtplib.SMTP("smtp.email.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Look Up\n\nThe ISS is above your in the sky."
    )