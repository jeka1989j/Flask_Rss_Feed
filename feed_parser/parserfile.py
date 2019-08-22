import feedparser
from flask import Flask

app = Flask(__name__)

# bbc_feed = 'http://feeds.bbci.co.uk/news/rss.xml'
rss_feeds = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}
# >>> parser = feedparser.parse(bbc_feed)
# >>> parser.keys()
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'href', 'status', 'encoding', 'version', 'namespaces'])

# >>> parser.entries[0].keys()
# dict_keys(['title', 'title_detail', 'summary', 'summary_detail', 'links', 'link', 'id', 'guidislink', 'published', 'published_parsed'])


@app.route('/')
@app.route('/<feed_name>')
def get_news(feed_name='bbc'):
    feed = feedparser.parse(rss_feeds[feed_name])
    first_article = feed['entries'][0]
    return """<html>
    <body>
    <h1>{3} Feed News</h1>
    <b>{0}</b></br>
    <p>{1}</p></br>
    <i>{2}</i>
    </body>
    </html>
    """.format(first_article.get("title"), first_article.get('summary'),
               first_article.get('published'), feed_name.upper())
