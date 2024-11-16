from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city: str):
    """Fetch the current weather for a given city."""
    api_key = "3a863f699a1a630235b4469b8ce1ec1a"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Formulate the request URL
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }

    try:
        # Make the HTTP GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        data = response.json()

        # Extract weather information
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temp}°C with {description}."
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return "Invalid city or response format."


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
        return render_template("index.html", weather=weather)
    return render_template("index.html", weather=None)

if __name__ == "__main__":
    app.run(debug=True)
