from flask import Flask
from flask import render_template, url_for, request
from werkzeug import secure_filename
import base64
import os
import file_tools
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('canvas.html')


@app.route('/ann', methods=['POST'])
def request_img():
    strs = request.get_data()
    strs = strs.split(',')
    imgdata = base64.b64decode(strs[1])
    with open('img.png', 'wb') as f:
        f.write(imgdata)
    num = file_tools.get_num('img.png')
    return num


if __name__ == '__main__':
    app.run(debug=True)
