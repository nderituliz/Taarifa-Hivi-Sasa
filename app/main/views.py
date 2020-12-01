from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, search_artciles
from ..models import Articles, Sources

# Views
@main.route('/')
def index():

    """
    Function that returns the index page and its data
    """
    general_categories = get_sources()

    
    title = 'Taarifa Hivi Sasa Highlights'
    search_articles = request.args.get('articles_querry')
    if search_articles:
        return redirect(url_for('search', articles_name=search_articles))
    else:
        return render_template('index.html',title = title, general = general_categories)
