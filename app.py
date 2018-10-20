from flask import Flask 
from pathlib import Path
import os


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    os.system('./waon -i happybirthday.wav -o birthday.mid')

f = Path('./birthday.mid')
if f.is_file():
    print('it here')