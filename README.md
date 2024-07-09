<div align="center">
  <img alt="PetHappy" src="https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness/blob/main/static/PetPeeve-banner.png?raw=true">
</div>

## About the Project
**[PetPeeve: Climate & Pet Wellness](https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness)** is a Flask web application that provides care tips based on the user's current weather and heat index. It utilizes a hashing and collision algorithm (hash table) implementation with a fast look up for O(1).

It comes with a little optimization such as hashing the first two letters and last letter of the key. To handle collision, this uses a load factor that indicates the fullness of hash table and maintains the complexity of O(1).


## Built With
* **HTML:** This builds the structure of the application.
* **CSS:** Used for adding styles.
* **Bootstrap:** CSS frameworks used for adding cards and containers.
* **JavaScript:** It was used for updating the page's display date and getting the user's location.
* **Python:** Used for building the hash table and rendering HTML.
* **Flask:** Python framework used to render HTML.
* **Geolocation:** It is an HTML API which returns the current position of the user.
* **[OpenWeatherMap](https://openweathermap.org/):** This API is necessary to get the heat index and temperature of a location based on the result from Geolocation.

## Folder Structure
    .
    │
    ├── static
    │   ├── clear.png
    │   ├── cloudy.png
    │   ├── location.png
    │   ├── pets.png
    │   ├── PetPeeve-banner.png
    │   ├── rainy.png
    │   ├── style.css
    │   ├── sunny.png
    │   
    ├── template
    │   │    ├── index.html
    │   │
    │   ├── .env_sample
    │       
    ├── app.py
    ├── hashTableImplementation.py
    ├── README.md
    ├── requirements.txt 

## Features
- **Climate-based pet care tips:** Allows users to determine the action they need to take to tend to their pet needs for specific weather conditions. 
- **User location integration:** Detects the user's location.
- **Custom hash table:** Implements a custom hash table which maintains a time complexity of O(1).
- **Responsive:** It support mobile and web devices for easy access.

## Installation
To get a local copy of the repository, follow these steps:

1. **Clone the repository:** Get started by cloning the repository to your local machine.
```sh
git clone https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness.git
```

2. **Locate project folder:** Navigate the folder where the project folder is stored using cd. 
  ```sh
  cd PetPeeve-Climate-Check-Pet-Wellness
  ```

3. **Set up a Python virtual environment:**
    - Type this command in your terminal or cmd:
    ```sh
    python -m venv .venv
    ```
    - Activate virtual environment: 
    ```sh
    .\.venv\Scripts\activate.bat
    ```

4. **Install dependencies:** It contains the packages needed for running the application
  ```sh
  pip install -r requirements.txt
  ```
6. **Add API key:** To get the weather information such as heat index and temperature, get the API key from [openweatherapp.org](https://openweathermap.org/) and navigate to .env_sample, then change it into .env where you should set the API_KEY on the API key you get from the Openweathermap.
  ```sh
  API_KEY=YOUR_API_KEY
  ```

7. **Run the application:**
```sh
python app.py
```
* Open your web browser and navigate to http://127.0.0.1:5000/.
* Allow location access when prompted.
* View pet care tips based on the current weather and heat index.

## Demo
<video src="./static/Demo-Installation.mp4" autoplay loop></video>

## Authors
- Chua, William Eduard M. ([@veenoise](https://github.com/veenoise))
- David, Abdurasheed A. ([@sheed](davidabdurasheed@gmail.com))
- Egera, Ashley I. ([@ash](ashleyegera.school@gmail.com))
- Rolle, Xavier B. ([@xavier](xavierbuen.rolle@gmail.co))
- Villasor, Cristina C. ([@ilhye](https://github.com/ilhye))
