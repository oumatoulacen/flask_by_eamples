from flask import Flask, render_template, request, redirect, url_for
import feedparser

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640',
    'nyt': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'aljazeera': 'http://www.aljazeera.com/xml/rss/all.xml',
    'guardian': 'https://www.theguardian.com/world/rss',
    'telegraph': 'http://www.telegraph.co.uk/news/rss.xml',
    'skynews': 'http://feeds.skynews.com/feeds/rss/world.xml',
    'daily_mail': 'http://www.dailymail.co.uk/news/index.rss',
    'mirror': 'http://www.mirror.co.uk/news/rss.xml',
    'independent': 'http://www.independent.co.uk/news/world/rss',
    'metro': 'http://metro.co.uk/news/world/feed/',
    'standard': 'http://www.standard.co.uk/news/world/rss',
    'evening_standard': 'http://www.standard.co.uk/news/rss',
    'sun': 'https://www.thesun.co.uk/news/worldnews/feed/'
    }

app = Flask(__name__)

@app.route("/<publication>")
def bbc(publication="bbc"):    
    feeds = feedparser.parse(RSS_FEEDS[publication])
    # print(feeds)
    return render_template("home.html", articles=feeds['entries'], publication=publication, channels=RSS_FEEDS)

@app.route("/")
def get_news():
    query = request.args.get("publication") or "bbc"
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home1.html",
        articles=feed['entries'], publication=publication, channels=RSS_FEEDS)


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