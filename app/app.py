from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import markovmodel_runner
import os
import dotenv
from requests_oauthlib import OAuth1Session


dotenv.load_dotenv('.env')
app = Flask(__name__)

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)


def tweet(status):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    resp = session.post(url, {'status': status})
    return resp.text


@app.route('/tweet', methods=['POST'])
def tweet_request():
    if request.method == 'POST':
        status = request.form['sentence']
        tweet(status)
    return redirect('/')


@app.route('/')
def run_model():
    result = markovmodel_runner.run(5, 4, 50)
    while result == '""':
        result = markovmodel_runner.run(5, 4, 60)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
