from flask import Flask
from responses import (mood_responses, temperature_responses,
                       heart_rate_responses, sleep_time_responses,
                       season_responses)

app = Flask(__name__)


@app.route("/mood/<string:mood>")
def mood(mood):
    if mood in mood_responses:
        return {"health_tip": mood_responses[mood]}
    else:
        # the mood is invalid return 404 status
        return {"error": "Mood not found"}, 404

@app.route("/temperature/<float(1):temperature>")
def temperature(temperature):
    good = 97.4, 99.4
    # temperature too low
    if temperature < good[0]:
        return {"health_tip": temperature_responses["low"]}
    # temperature too high
    if temperature > good[1]:
        return {"health_tip": temperature_responses["high"]}
    # temperature is good
    return {"health_tip": temperature_responses["good"]}

@app.route("/heart_rate/<int:heart_rate>")
def heart_rate(heart_rate):
    good = 60, 100
    # heart rate too low
    if heart_rate < good[0]:
        return {"health_tip": heart_rate_responses["low"]}
    # heart rate too high
    if heart_rate > good[1]:
        return {"health_tip": heart_rate_responses["high"]}
    # heart rate is good
    return {"health_tip": heart_rate_responses["good"]}

@app.route("/sleep/<int:sleep_time>")
def sleep(sleep_time):
    good = 7, 8
    # sleep time too low
    if sleep_time < good[0]:
        return {"health_tip": sleep_time_responses["low"]}
    # sleep time too high
    if sleep_time > good[1]:
        return {"health_tip": sleep_time_responses["high"]}
    # sleep time is good
    return {"health_tip": sleep_time_responses["good"]}

@app.route("/season/<string:season>")
def season(season):
    if season in season_responses:
        return {"health_tip": season_responses[season]}
    else:
        # the season is invalid return appropriate status
        return {"error": "Season not found"}, 404