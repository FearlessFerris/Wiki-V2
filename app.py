# Main Wiki-V2 Application 

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from models import db, connect_db, User, Search, Favorite, Friend, Chat 

import requests
from bs4 import BeautifulSoup



app = Flask( __name__ ) # Create an instance of Flask Class and assign to the variable App 
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql:///wiki-v2' # Specify the connection string that SQLAlehemy will use to connect to the PostgreSQL Database ( URI = Uniform Resource Identifier )
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False # Track modifications to objects and emit signals when changes occur 
app.config[ 'SQLALCHEMY_ECHO' ] = True # Print all SQL statements it executes in the terminal


get_page_html = 'https://en.wikipedia.org/w/rest.php/v1/page/' # Base url for page-information 

@app.route( '/', methods = ['GET', 'POST'] )
def homepage():
    """ Application Homepage """

    return render_template( 'homepage.html' )

@app.route( '/page/<title>', methods = ['GET', 'POST'] )
def get_info( title ):
    """ Appends Page information for user """

    try:

        res = requests.get( f'{ get_page_html }{ title }/html' )
        if res.status_code != 200:
            return render_template( 'error.html', message = 'Failed to recieve page information' )

        resHtml = BeautifulSoup( res.text, 'html.parser' )

        base_tags = resHtml.find_all( 'base' )
        for base_tag in base_tags:
            base_tag[ 'href' ] = 'http://127.0.0.1:5000/'

        style_tags = resHtml.find_all(lambda tag: tag.name == 'link' and 'rel' in tag.attrs and tag.attrs['rel'] == ['stylesheet'])

        for style_tag in style_tags:
            style_tag.extract()

        html = resHtml.prettify()
        
        return render_template( 'page.html', title = title, html = html )

    except requests.RequestException as e:
        return render_template( 'error.html', message = 'Failed to retrieve page information: {}' .format( e ))
    
     
    









