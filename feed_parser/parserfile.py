import feedparser
from flask import Flask, render_template, request, make_response
from .parse_weather import get_weather
from .parse_currency import get_currency
from datetime import datetime, timedelta

app = Flask(__name__)

# bbc_feed = 'http://feeds.bbci.co.uk/news/rss.xml'
rss_feeds = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}

default = {'feed_name': 'bbc', 'city': 'Kyiv',
           'currency_from': 'usd', 'currency_to': 'uah'}


def get_response_value(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return default[key]


@app.route('/')
def home():
    feed_name = request.args.get('news_feed')
    if not feed_name:
        feed_name = request.cookies.get('news_feed')
        if not feed_name:
            feed_name = default['feed_name']
    # feed_name = get_response_value('feed_name')
    articles = get_news(feed_name)
    # city = request.args.get('city')
    # if not city:
    #     city = default['city']
    city = get_response_value('city')
    weather = get_weather(city)
    # currency_from = request.args.get('currency_from')
    # if not currency_from:
    #     currency_from = default['currency_from']
    currency_from = get_response_value('currency_from')
    # currency_to = request.args.get('currency_to')
    # if not currency_to:
    #     currency_to = default['currency_to']
    currency_to = get_response_value('currency_to')
    rate, currencies = get_currency(currency_from, currency_to)
    response = make_response(render_template('feed_news.html', news=articles,
                                             weather=weather, currency_from=currency_from,
                                             currency_to=currency_to, rate=rate,
                                             currencies=currencies))
    expires = datetime.now() + timedelta(minutes=30)
    response.set_cookie('news_feed', feed_name, expires=expires)
    response.set_cookie('city', city, expires=expires)
    response.set_cookie('currency_from', currency_from, expires=expires)
    response.set_cookie('currency_to', currency_to, expires=expires)
    return response

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
