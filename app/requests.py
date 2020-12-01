import urllib.request,json
from .models import Sources, Articles


api_key = None


base_url = None
base_article_url = None

def configure_request(app):
    global api_key, base_url, base_article_url
    api_key = app.config ["NEWS_API_KEY"]
    base_url = app.config ["NEWS_API_BASE_URL"]
    base_article_url = app.config["ARTICLES_API_BASE_URL"]