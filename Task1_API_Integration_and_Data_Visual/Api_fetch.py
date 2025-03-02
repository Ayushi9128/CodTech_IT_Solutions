import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# API details
api_key= '688f5947a13d0cad077d998bb9031a66'
api_url=f'https://api.openweathermap.org/data/2.5/forecast'

c = "Delhi"
p = {
    "q": c,
    "appid": api_key,
    "units": "metric"
}

# Fetching data from the API
response = requests.get(api_url, params=p)
data = response.json()

if response.status_code == 200:
    
    dates = []
    temp = []
    humidity = []
    
    for entry in data['list']:
        dates.append(datetime.datetime.fromtimestamp(entry['dt']))
        temp.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])
    
    
    sns.set(style="whitegrid")

    # data visualiaztions
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temp, label='Temperature (°C)', color='red', marker='o')
    plt.title(f"Temperature Trend for {c}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=35)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(dates, humidity, label='Humidity (%)', color='blue', marker='o')
    plt.title(f"Humidity Trend for {c}")
    plt.xlabel("Date & Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=35)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to fetch data: {data.get('message', 'Unknown error')}")
