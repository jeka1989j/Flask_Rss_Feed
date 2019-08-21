import feedparser
from flask import Flask

app = Flask(__name__)

bbc_feed = 'http://feeds.bbci.co.uk/news/rss.xml'


@app.route('/')
def get_news():
    feed = feedparser.parse(bbc_feed)
    print(feed)
