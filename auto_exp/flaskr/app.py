from os import system
from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crawl')
def start_crawler():
    a = system('python -m scrapy crawl yy')
    return jsonify({'result': a})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
