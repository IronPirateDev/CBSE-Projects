from flask import Flask, render_template, request, redirect, send_from_directory
from flask import Flask, session, flash
import os
from flask import flash, redirect, url_for
app = Flask(__name__, static_folder='templates/static')
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')