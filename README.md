# Project Overview: CI/CD Weather Application
This is a simple weather web application built using Flask. It integrates automated testing and a CI/CD pipeline to ensure the codebase is always reliable and secure. Below is a step-by-step explanation of the process involved in creating, testing, and deploying the application.

## Steps to Build the Project

### 1. **Create the Flask Application**
- Set up a Python environment and install Flask.
- Develop the `app.py` file, which contains:
  - A function `get_weather` to fetch weather data from the OpenWeatherMap API.
  - The Flask app routes, including the main route `/`, to accept city input from users and display the weather.

### 2. **Design the HTML Template**
- Create an `index.html` file in a `templates` directory.
- Use Flask's `render_template` function to dynamically display the weather data or errors based on the user’s input.

### 3. **Write Unit Tests**
- Create a `test_app.py`.
- Write unit tests for the `get_weather` function using the `pytest` library.
- Use `unittest.mock` to mock API calls and simulate both successful and failed responses.

### 4. **Set Up Dependencies**
- Create a `requirements.txt` file with all necessary dependencies (e.g., `Flask`, `pytest`, `requests`).
- Use `pip` to install dependencies locally during development and within the pipeline.

### 5. **Set Up a CI/CD Pipeline**
- Use GitHub Actions for the CI/CD pipeline.
- Create a `.github/workflows/ci.yml` file to define the pipeline steps:
  1. Check out the repository code.
  2. Set up the Python environment.
  3. Install dependencies (`pip install -r requirements.txt`).
  4. Run unit tests (`pytest`)..

### 6. **Run Locally and Test**
- Run the Flask application locally using `python app.py`.
- Navigate to `http://localhost:5000` to interact with the application.
- Use `pytest` to run the unit tests locally to verify functionality.

### 7. **Push to GitHub and Verify Pipeline**
- Push the code to a GitHub repository.
- Check the pipeline status in the Actions tab of the repository.
- Ensure all tests and checks pass in the pipeline before making changes to the `main` branch.

---

## How It Works
- **User Interaction**: The user inputs a city name, and the app fetches the current weather using the OpenWeatherMap API.
- **Error Handling**: The app gracefully handles errors such as invalid city names or network issues.
- **Automated Testing**: Unit tests ensure the API interactions and app logic work as expected, even simulating API failures.
- **CI/CD Pipeline**: The pipeline automatically:
  - Runs tests.
  - Ensures every code change is tested before deployment.


## Key Learnings
This project demonstrates the integration of application development with modern DevOps practices, focusing on:
1. Flask web development.
2. Writing testable and maintainable Python code.
3. Using GitHub Actions to automate testing and security analysis.
4. Building a secure, production-ready workflow.

---

## Running the Project
1. Clone the repository: `git clone https://github.com/estheresom17/ci-cd-pipeline.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app locally: `python app.py`.
4. Test the app: `pytest`.
5. Push changes to GitHub to trigger the CI/CD pipeline.
