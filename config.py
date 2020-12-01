import os
class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey=fb94d5e25c0c4415b3e09b25c25b3d62'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fb94d5e25c0c4415b3e09b25c25b3d62'

    NEWS_API_KEY = os.environ.get('fb94d5e25c0c4415b3e09b25c25b3d62')
    
    SECRET_KEY= os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    """
    Pruduction  configuration child class
    """
        
    pass
    
class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True
config_options = {
 'development' : DevConfig,
 'production' : ProdConfig
}