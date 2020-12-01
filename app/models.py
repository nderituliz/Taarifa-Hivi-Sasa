class Sources:
    """
    Source class to define the source of news
    """
    
    def __init__(self, id, name, description, url, newsCategory, language, country):
        self.id= id
        self.name = name
        self.description = description
        self.url = url
        self.newsCategory = newsCategory
        self.language = language
        self.country = country
        