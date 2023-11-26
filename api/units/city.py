import requests
from datetime import datetime


def getcity(ip):
    # location = requests.get(
    #     "https://api.ipgeolocation.io/ipgeo?apiKey=a48546dd2cbd4078bba83832fdc62b6e&ip=105.158.18.79").json()
    location = requests.get(
        "https://api.ipgeolocation.io/ipgeo?apiKey=a48546dd2cbd4078bba83832fdc62b6e&ip={}".format(ip)).json()
    # ++++++++++++++++
    # location = requests.get(
    #     "http://ip-api.com/json/?fields=61439&ip={}".format(ip)).json()
    if "city" not in location:
        return ""
    return location['city']


def getweather(city, language="en"):
    res = requests.get(
        "https://api.weatherapi.com/v1/forecast.json?key=826454625a09464da3730135232411&q={}&lang={}&days=7".format(city, language))
    if res.status_code != 200:
        return {}
    weather = res.json()
    obj = {}
    obj["name"] = weather["location"]["name"]
    obj["condition"] = weather["current"]["condition"]["text"]
    obj["temp_c"] = str(weather["current"]["temp_c"]).split('.')[0]
    obj["temp_c"] += 'C°'
    obj["temp_f"] = str(weather["current"]["temp_f"]).split('.')[0]
    obj["temp_f"] += 'F°'
    day = weather["forecast"]["forecastday"][0]["day"]
    prob = {"daily_will_it_rain": 0, "daily_chance_of_rain": 0,
            "daily_will_it_snow": 0, "daily_chance_of_snow": 0}
    for key in day:
        if key in prob:
            prob[key] = day[key]
    bigkey = 'daily_chance_of_rain'
    for key in prob:
        if prob[key] > prob[bigkey]:
            bigkey = key
    argtx = bigkey.split('_')
    obj["text"] = "{}: {}%".format(" ".join(argtx[1:]), prob[bigkey])
    needs = ["feelslike_c",
             "feelslike_f",
             "uv",
             "wind_mph",
             "wind_kph",
             "wind_degree",
             "wind_dir"]
    for key in weather["current"]:
        if key in needs:
            if key.startswith("feelslike"):
                obj[key] = "{}: {}{}°".format("Real feel",
                                              weather["current"][key], key.split('_')[1].upper())
            else:
                obj[key] = "{}: {}".format(" ".join(key.split('_')),
                                           weather["current"][key])

    """
    "daily_will_it_rain": 0,
    "daily_chance_of_rain": 0,
    "daily_will_it_snow": 0,
    "daily_chance_of_snow": 0,
    """
    hour = weather["forecast"]["forecastday"][0]["hour"]
    obj["day"] = {}
    for elm in hour:
        if (int(elm["time"][-5:-3]) + 2) % 4 == 0:
            dictionary = {}
            dictionary["temp_c"] = "{}C°".format(
                str(elm["temp_c"]).split('.')[0])
            dictionary["temp_f"] = "{}F°".format(
                str(elm["temp_f"]).split('.')[0])
            dictionary["condition"] = elm["condition"]["text"]
            obj["day"][elm["time"][-5:]] = dictionary

    week = []
    for day in weather["forecast"]["forecastday"]:
        date_object = datetime.strptime(day["date"], '%Y-%m-%d')
        week.append({'day_name': date_object.strftime('%A'),
                    'condition': day["day"]["condition"]["text"],
                     'temp_c': ["{}".format(
                         str(day['day']["maxtemp_c"]).split('.')[0]), "{}".format(
                         str(day['day']["mintemp_c"]).split('.')[0])],
                     'temp_f': ["{}".format(
                         str(day['day']["maxtemp_f"]).split('.')[0]), "{}".format(
                         str(day['day']["mintemp_f"]).split('.')[0])]})
        week[0]['day_name'] = 'today'
    obj['weekly'] = week
    return obj
