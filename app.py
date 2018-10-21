import os
from flask import Flask, flash, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set('mid')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()
    os.system('waon -i happybirthday.wav -o birthday.mid')
    if open('birthday.mid'):
        print('yea')