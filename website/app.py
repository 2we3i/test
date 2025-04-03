from flask import Flask, render_template
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Загружаем переменные из .env
load_dotenv()
INVITE_LINK = os.getenv('INVITE_LINK')

@app.route('/')
def index():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', 
                          messages=data["messages"], 
                          online_count=data["online_count"], 
                          invite_link=INVITE_LINK)

if __name__ == '__main__':
    app.run(debug=True)