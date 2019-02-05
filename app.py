from flask import Flask, render_template, request, url_for
from flask_bootstrap import flask_bootstrap


from textblob import TextBlob, Word 
import random
import io



app = Flask(__name__)

@app.router('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)