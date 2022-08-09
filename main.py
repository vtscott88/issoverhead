import requests
from datetime import datetime, timezone

MY_LAT = 40.728670 # Your latitude
MY_LONG = -75.202440 # Your longitude

def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.  Create function returns true if within +5 or -5
    if iss_latitude - 5.0 <= MY_LAT <= iss_latitude + 5.0 and iss_longitude - 5.0 <= MY_LONG <+ iss_longitude + 5.0:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)
print(sunrise)
print(sunset)
print(time_now.hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if check_position() and time_now.hour > sunset:
    print("Overhead")


