from flask import Flask
import markovmodel_runner

app = Flask(__name__)


@app.route('/')
def run_model():
    return markovmodel_runner.run(5, 4, 200)

if __name__ == '__main__':
    app.run()
