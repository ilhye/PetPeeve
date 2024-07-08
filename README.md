# PetPeeve: Climate Check & Pet Wellness
This is a Flask web application that provides pet care tips based on the user's current weather and heat index. It utilizes a custom hashing and collision algorithm (hash table) implementation with a fast look up of O(1).

## Authors

- [@ilhye](https://github.com/ilhye)
- [@veenoise](https://github.com/veenoise)

## Features
- Climate-based pet care tips.
- User location integration.
- Custom hash table implementation for efficient data retrieval.

## Deployment
1. Locate project folder:
```
    cd source
```

2. Set up a Python virtual environment:
```
    python -m venv .venv
```

3. Activate virtual environment:
```
    .\.venv\Scripts\activate.bat
```
4. Install dependencies:
```
    pip install -r requirements.txt
```

5. Run the application:
```
    python app.py
```

## Usage/Examples
1. Open your web browser and navigate to http://127.0.0.1:5000/.
2. Allow location access when prompted.
3. View pet care tips based on the current weather and heat index.
