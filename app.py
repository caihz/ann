from flask import Flask
from flask import render_template,url_for,request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('canvas.html')


@app.route('/ann', methods=['POST'])
def request_img():
	print request.get_data()
	return 'success'


if __name__ == '__main__':
    app.run()