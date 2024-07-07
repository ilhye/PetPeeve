from flask import Flask, render_template, url_for
from hashTableImplementation import PET_CARE_TIP
from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_KEY = getenv('API_KEY')   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', API_KEY=API_KEY)


app.run(
    debug=True
)