from flask_speech_recognition import RecognitionEngine
from flask import Flask

app = Flask(__name__)
engine = RecognitionEngine()
app.config['SERVICE_NAME'] = '通义千问'
app.config['ENGINE'] = engine

app.wsgi_app = engine

app.run(port=8080, debug=True)