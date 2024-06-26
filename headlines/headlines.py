import feedparser
from flask import Flask

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'}

app = Flask(__name__)

@app.route("/")
@app.route("/<publication>")
def bbc(publication="bbc"):
    if publication not in RSS_FEEDS:
        publication = "bbc"
    return get_news(publication)

def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
    <body>
    <h1>Headlines </h1>
    <b>{0}</b> </ br>
    <i>{1}</i> </ br>
    <p>{2}</p> </ br>
    </body>
    </html>""".format(first_article.get("title"), first_article.
    get("published"), first_article.get("summary"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)