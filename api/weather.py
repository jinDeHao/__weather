from flask import Flask, Blueprint, make_response, render_template, request
from flask_cors import CORS
import requests
from .units.city import getcity, getweather
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def auto():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    city = getcity(client_ip)
    weather = getweather(city)
    if weather == {}:
        return render_template('no_ip.html')
    return render_template('weather.html',  weather=weather)


@app.route('/<city>')
def status_ok(city=""):
    print(city)
    # if city == "":
    #     client_ip = request.remote_addr
    #     city = getcity(client_ip)
    #     weather = getweather(city)
    #     if weather == {}:
    #         return render_template('no_ip.html')
    #     return render_template('weather.html',  weather=weather)
    weather = getweather(city)
    if weather == {}:
        return render_template('no_ip.html')
    return render_template('weather.html',  weather=weather)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, threaded=True)
