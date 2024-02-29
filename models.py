# Wiki-V2 Application Models 

from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import DateTime
from datetime import datetime 



db = SQLAlchemy() # Initialize an instance of the SQLAlchemy class 



class User( db.Model ): 
    
    """ User Model """

    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.Text, nullable = False, unique = True )
    password = db.Column( db.Text, nullable = False )
    email = db.Column( db.Text, nullable = False, unique = True )
    dob = db.Column( db.Text, nullable = True )
    image_url = db.Column( db.Text, nullable = False )

    def __init__( self, username, password, email, image_url, dob = None ):
        """ Initialize User """ 
        self.username = username 
        self.password = password 
        self.email = email
        self.image_url = image_url
        self.dob = dob 

    def __repr__( self ):
        """ Representation Method of User Instance """
        return f"User( id = { self.id }, username = '{ self.username }', password = '{ self.password }', email = '{ self.email }', image_url = '{ self.image_url }')"

    
class Search( db.Model ):
    """ Search Model """

    __tablename__ = 'searches'

    id = db.Column( db.Integer, primary_key = True )
    term = db.Column( db.Text, nullable = False )
    time = db.Column( db.DateTime, default = datetime.utcnow, nullable = False )
    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ), nullable = False )
    user = db.relationship( 'User', backref = 'searches' )

    def __repr__( self ):
        """ Representation method of A Search Instance """
        return f"Search( term = '{ self.term }', time = '{ self.time }', user_id = '{ self.user_id}')"



class Favorite( db.Model ):
    
    """ Favorite Model """

    __tablename__ = 'favorites'

    id = db.Column( db.Integer, primary_key = True, nullable = False )
    page = db.Column( db.Text, nullable = False, unique = True )
    time = db.Column( db.DateTime, default = datetime.utcnow, nullable = False )
    user_id = db.Column( db.Integer, db.ForeignKey( 'users_id' ), nullable = False )
    user = db.relationship( 'User', backref = 'favorites' )

    def __repr__( self ):
        """ Representation Method of A Favorite Instance """
        return f"Favorite( page = '{ self.page }', time = '{ self.time }', user_id = '{ self.user_id }')"



class Friend( db.Model ):
    
    """ Friend Model """

    __tablename__ = 'friends'

    id = db.Column( db.Integer, primary_key = True, nullable = False )
    username = db.Column( db.Text, nullable = False )
    user_id = db.Column( db.Integer, db.ForeignKey( 'users_id' ), nullable = False, unique = True )
    user_image_url = db.Column( db.Text, db.ForeignKey( 'users_image_url' ), nullable = True )
    user = db.relationship( 'Users', backref = 'friends')

    def __repr__( self ):
        """ Representation of A Friend Instance """
        return f"Friend( username = '{ self.username }', user_id = '{ self.user_id }', user_image_url = '{ self.user_image_url }' )"



class Chat( db.Model ):
    """ Chat Model """

    __tablename__ = 'chats'

    id = db.Column( db.Integer, primary_key = True, nullable = False )
    message = db.Column( db.Text, nullable = False )
    time = db.Column( db.Text, nullable = False )
    sender_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ), nullable = False )
    reciever_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ), nullable = False )
    sender = db.relationship( 'User', foreign_keys = [ sender_id ], backref = 'sent_messages' )
    reciever = db.relationship( 'User', foreign_keys = [ reciever_id ], backref = 'recieved_messages' )

    def __repr__( self ):
        """ Representation of A Chat Instance """
        return f"Chat( message = '{ self.message}', time = '{ self.time }', sender_id = '{ self.sender_id }', reciever_id = '{ self.reciever_id }' )"



def connect_db( app ):
    """ Connect to Database """

    db.app = app
    db.init_app( app )