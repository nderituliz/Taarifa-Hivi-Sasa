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

def get_sources():
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)
            print(sources_results_list, '1234')
            
    return sources_results