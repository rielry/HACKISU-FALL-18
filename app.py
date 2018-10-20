from flask import Flask 
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    os.system('waon -i happybirthday.wav -o birthday.mid')
    if open('birthday.mid'):
        print('yea')