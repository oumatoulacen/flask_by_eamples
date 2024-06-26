from flask import Flask, render_template
import feedparser

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'}

app = Flask(__name__)

@app.route("/")
@app.route("/<publication>")
def bbc(publication="bbc"):    
    feeds = feedparser.parse(RSS_FEEDS[publication])
    # print(feeds)
    return render_template("home.html", articles=feeds['entries'])


@app.route("/print_ansi")
def print_ansi():
    # ANSI escape codes for red color and reset
    RED = '\033[91m'
    RESET = '\033[0m'

    # Your print statement with ANSI color codes
    print(f'{RED}cnn news:{RESET} {RSS_FEEDS["bbc"]}')
    return f'{RED}cnn news:{RESET} {RSS_FEEDS["bbc"]}'


if __name__ == "__main__":
    app.run(port=5000, debug=True)