import os
from flask import Flask, flash, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set('mid')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
	return render_template('index.html')

#Check if filetype is allowed because fuck trusting your users
def allowed_file(filename):
	return filename.rsplit('.', 1)[1].lower() == 'mid'

@app.route('/getblob', methods = ['POST'])
def get_post_javascript_data():
	print(request.form)
	return "hey it worked <3"

#File Upload Logic
@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)
		
		file = request.files['file']
		print(allowed_file(file.filename))
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			print('No selected file')
			return redirect(request.url)
		if allowed_file(file.filename):           
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
			return 'Upload succeeded!'
			#return redirect(url_for('uploaded_file', filename=filename))
	return 'Upload failed!'

#Main application logic
if __name__ == '__main__':
	app.secret_key = 'XD'
	app.config['SESSION_TYPE'] = 'filesystem'

	app.debug = True
	app.run()