import re
import random
from flask import Flask, render_template, request, redirect, url_for
from string import ascii_letters, digits

app = Flask(__name__)

PARAM = ascii_letters + digits

urls = {}

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/traitement', methods=["POST"])
def traitement():
    url = request.form
   
    while True:
        short_code_url = "".join(random.sample(PARAM, 3))
        if short_code_url not in url:
            short_url = "http://127.0.0.1:5000/" + short_code_url
            urls[short_code_url] = url.get('url')
            return render_template("index.html", short_url=short_url)

@app.route('/<short_code_url>')
def short_to_long_url(short_code_url):
    code_url=short_code_url
    if code_url in urls:
        long_url = urls[code_url]
        return redirect(long_url)
    else:
        return "404, verifier votre lien"
