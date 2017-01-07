from flask import Flask
from flask import render_template,url_for,request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('canvas.html')

if __name__ == '__main__':
    app.run()