from os import system
from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crawl')
def start_crawler():
    system('python -m scrapy crawl yy')
    return jsonify({'result': 'Task created'})


if __name__ == '__main__':
    app.run()
