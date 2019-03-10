from flask import Flask
from flask import render_template
from flask import flash, redirect, url_for, request, session
import csv, os, datetime

app = Flask(__name__)
app.secret_key = 'bss'

@app.route('/')
def top():
    tweets = [[]]
    path = "data/tweets.csv"
    if os.path.exists(path):
        with open(path) as f:
            reader = csv.reader(f, delimiter='\t')
            tweets = [row for row in reader]

    return render_template('top.html', title="ひとことBSS", tweets=tweets)

@app.route('/tweets', methods=['GET'])
def newTweet():
    return render_template('new.html', title="新規投稿")

@app.route('/create', methods=['POST'])
def createTweet():
    error = None
    username = request.form['username']
    tweet = request.form['tweet']
    if (len(username) == 0):
        error = '名前は必須です。'
        return render_template('new.html', title="新規投稿", error=error, username=username, tweet=tweet)

    if (len(username) > 20):
        error = '名前が20文字を越えています。'
        return render_template('new.html', title="新規投稿", error=error, username=username, tweet=tweet)

    if (len(tweet) == 0):
        error = 'つぶやきは必須です。'
        return render_template('new.html', title="新規投稿", error=error, username=username, tweet=tweet)

    if (len(tweet) > 100):
        error = 'ツイートが100文字を越えています。'
        return render_template('new.html', title="新規投稿", error=error, username=username, tweet=tweet)

    dt_now = datetime.datetime.now()
    with open('data/tweets.csv', 'a') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow([username, tweet, dt_now.strftime('%Y/%m/%d %H:%M:%S')])

    flash('投稿しました。')
    return redirect(url_for('top'))

if __name__ == '__main__':
    app.debug = True
    app.run()