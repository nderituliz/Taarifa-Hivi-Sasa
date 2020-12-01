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

def process_sources_results(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects
    """
    
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        newsCategory = source_item.get('newsCategory')
        language = source_item.get('language')
        country = source_item.get('country')
        
        # if poster:
        source_object = Sources(id, name, description, url, newsCategory, language, country)
        sources_results.append(source_object)

    print(sources_results)

    return sources_results

def get_articles(id):
    """
    Function that gets the json Articles response to our url request
    """
    get_articles_url = base_article_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def process_articles_results(articles_list):
    """
    Function  that processes the articles result and transform them to a list of Objects
    """
    
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        title = article_item.get('name')
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id, title, author, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results

def search_artciles(articles_name):
    
    search_articles_url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(api_key,articles_name)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['results']:
            search_articles_list = search_articles_response['results']
            search_articles_results = process_articles_results(search_articles_list)


    return search_articles_results

