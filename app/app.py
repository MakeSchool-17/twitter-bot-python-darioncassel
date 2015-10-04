from flask import Flask
import markovmodel_runner
import os

app = Flask(__name__)


@app.route('/')
def run_model():
    return markovmodel_runner.run(5, 4, 200)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
