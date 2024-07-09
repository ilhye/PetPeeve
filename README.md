<div align="center">
  <img width="200" alt="PetHappy" src="https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness/blob/main/static/pets.png">
</div>


# PetPeeve: Climate Check & Pet Wellness
This is a Flask web application that provides pet care tips based on the user's current weather and heat index. It utilizes a custom hashing and collision algorithm (hash table) implementation with a fast look up of O(1).

<div align="center">
  <img alt="PetHappy" src="https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness/blob/main/static/OutputSS.PNG">
</div>

![HTML](https://img.shields.io/badge/HTML-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-blueviolet.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=white) ![Python](https://img.shields.io/badge/Python-1572B6.svg?style=for-the-badge&logo=Python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)
## API

## Folder Structure
    .
    │
    ├── static
    │   ├── clear.png
    │   ├── cloudy.png
    │   ├── location.png
    │   ├── pets.png
    │   ├── rainy.png
    │   ├── style.css
    │   ├── sunny.png
    │   │ 
    │   ├── template
    │   │    ├── index.html
    │   │
    │   ├── .env
    │       
    ├── app.py
    ├── hashTableImplementation.py
    ├── requirements.txt 

## Features
- Free and open-source
- Climate-based pet care tips.
- User location integration.
- Custom hash table implementation for efficient data retrieval.
- Support mobile devices

## Usage
1. Clone this repository
```
    git clone https://github.com/ilhye/PetPeeve-Climate-Check-Pet-Wellness.git
```

2. Locate project folder:
```
    cd PetPeeve-Climate-Check-Pet-Wellness
```

3. Set up a Python virtual environment:
```
    python -m venv .venv
```

4. Activate virtual environment:
```
    .\.venv\Scripts\activate.bat
```
5. Install dependencies:
```
    pip install -r requirements.txt
```
6. Add API key from [openweatherapp.org](https://openweathermap.org/) in .env file
```
    API_KEY=YOUR_API_KEY
```

7. Run the application:
```
    python app.py
```
8. Open your web browser and navigate to http://127.0.0.1:5000/.
9. Allow location access when prompted.
10. View pet care tips based on the current weather and heat index.

## Authors
- Chua, William Eduard M. ([@veenoise](https://github.com/veenoise))
- David, Abdurasheed A.
- Egera, Ashley I.
- Rolle, Xavier
- Villasor, Cristina C. ([@ilhye](https://github.com/ilhye))
