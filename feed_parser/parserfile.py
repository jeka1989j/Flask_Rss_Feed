import feedparser
from flask import Flask, render_template, request
from .parse_weather import get_weather

app = Flask(__name__)

# bbc_feed = 'http://feeds.bbci.co.uk/news/rss.xml'
rss_feeds = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}

default = {'feed_name': 'bbc', 'city': 'Kyiv'}


@app.route('/')
def home():
    feed_name = request.args.get('news_feed')
    if not feed_name:
        feed_name = default['feed_name']
    articles = get_news(feed_name)
    city = request.args.get('city')
    if not city:
        city = default['city']
    weather = get_weather(city)
    return render_template('feed_news.html', news=articles, weather=weather)


# @app.route('/', methods=['GET', 'POST'])
def get_news(feed):
    # feed_name = request.form.get('news_feed')
    if not feed or feed.lower() not in rss_feeds:
        news_feed = default['feed_name']
    else:
        news_feed = feed.lower()
    feed = feedparser.parse(rss_feeds[news_feed])
    # weather = get_weather('Kyiv')
    # return render_template('feed_news.html', news=feed['entries'], weather=weather)
    return feed['entries']
