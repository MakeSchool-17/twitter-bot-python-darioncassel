from flask import Flask
from flask import render_template
import markovmodel_runner
import os

app = Flask(__name__)


@app.route('/')
def run_model():
    result = markovmodel_runner.run(5, 4, 50)
    while result == '""':
        result = markovmodel_runner.run(5, 4, 60)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
