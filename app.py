from flask import Flask, render_template
from responses import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# handle 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Invalid endpoint"}, 404

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/mood/<string:mood>")
def mood(mood):
    if mood == "stormy" or mood == "anxiety":
        return {"health_tip": mood_responses[mood]}
    else:
        # the mood is invalid return 404 status
        return {"error": "Mood not found"}, 404

@app.route("/temperature/<string:change>")
def temperature(change):
    if change == "increase" or change == "decrease":
        return {"health_tip": temperature_responses[change]}
    else:
        # the temperature change is invalid return 404 status
        return {"error": "Temperature change not found"}, 404
    
@app.route("/working-out-time/<string:change>")
def working_out_time(change):
    if change == "increase":
        return {"health_tip": working_out_time_responses[change]}
    else:
        # the working out time change is invalid return 404 status
        return {"error": "Working out time change not found"}, 404
    
@app.route("/physical-activity/<string:change>")
def physical_activity(change):
    if change == "decrease":
        return {"health_tip": physical_activity_responses[change]}
    else:
        # the physical activity change is invalid return 404 status
        return {"error": "Physical activity change not found"}, 404

@app.route("/heart-rate/<string:change>")
def heart_rate(change):
    if change == "improve" or change == "decrease":
        return {"health_tip": heart_rate_responses[change]}
    else:
        # the heart rate change is invalid return 404 status
        return {"error": "Heart rate change not found"}, 404

@app.route("/sleep-time/<string:change>")
def sleep(change):
    if change == "increase" or change == "reduce":
        return {"health_tip": sleep_time_responses[change]}
    else:
        # the sleep change is invalid return 404 status
        return {"error": "Sleep change not found"}, 404

