from flask import Flask, render_template, url_for, request, jsonify
from hashTableImplementation import PET_CARE_TIP
from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_KEY = getenv('API_KEY')   

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        int_heat_index = None
        int_weather = None
        data = request.json
        heat_index = data['heatIndex']
        weather = data['weather']
                
        match heat_index:
            case 'Caution':
                int_heat_index = 0
            case 'Extreme Caution':
                int_heat_index = 1
            case 'Danger':
                int_heat_index = 2
            case 'Extreme Danger':
                int_heat_index = 3

        match weather:
            case 'Clear':
                int_weather = 0
            case 'Cloudy':
                int_weather = 1
            case 'Rainy':
                int_weather = 2
            case 'Sunny':
                int_weather = 3

        cat = PET_CARE_TIP.access(int_weather, int_heat_index, 'cat')  
        dog = PET_CARE_TIP.access(int_weather, int_heat_index, 'dog')        
        combine = [cat, dog]
        
        return jsonify(combine)
    return render_template('index.html', API_KEY=API_KEY)


app.run(
    debug=True
)