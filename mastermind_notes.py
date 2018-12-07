#! /usr/bin/python

# print('Content-type: text/html')
# print('')
# print("Hello Galaxy!")

# from flask import flask
# app = Flask(__name__)

# @app.route('/') - Root page of site
# def hello_world():
#     return('Hello World!')

# import mysql.connector

# MySQL:
    # shareddb-f.hosting.stackcp.net
    # mastermind-36399dc7
    # urcmvptz35

# Virtual environment
    # cd /Users/Tobias/Documents/Development/Projects/2018_Projects/Mastermind/
    # conda create --name Mastermind_env flask sqlalchemy numpy pandas
    # conda activate Mastermind_env
    # Export environment
        # conda env export > environment.yaml
        # cat environment.yaml
        # to load this environment
            # conda create -f environment.yaml
    # Environment variables
        # conda env list
        # cd /anaconda3/envs/Mastermind_env
        # mkdir -p etc/conda/activate.d
        # mkdir -p etc/conda/deactivate.d
        # touch etc/conda/activate.d/env_vars.sh
        # touch etc/conda/deactivate.d/env_vars.sh
            # code . (to open in VSCode)
            # added DATABASE_URI=''
            # ^^ NEED TO FIND OUT HOW TO SET THAT CORRECTLY 

# Templates
    # create directory for Templates
    # create:
        # html files for each page (if unique code)
        # layout.html to easily be able to edit layout of all pages at once
        # main.css
    # link:
        # render_template
            # inside curly brackets + percent put the {% python code %} 
            # e.g.  
                #   {% extends "layout.html" %}
                #       {% block ____ %}
                #           {% for posts in posts %} 
                #               <h2>{{ posts.user }}</h2>
                #           {% endfor %}
                #       {% endblock ____ %}
        # return render_template('___.html', posts=posts)
        # part of "layout.html" header section
            # <link rel="stylesheet" type="text/css" 
                #   href="{{ url_for('static', filename='main.css') }}"
                #   >

                # {% if title %}
                #   <title>Mastermind - {{ title }}</title>
                # {% else %}
                #   <title>Mastermind</title>
                # {% endif %}

# Database 
    # (Mastermind_env) Tobiass-MacBook-Pro:Mastermind Tobias$ python
    # Python 3.7.1 (default, Oct 23 2018, 14:07:42) 
    # [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    # Type "help", "copyright", "credits" or "license" for more information.
    # >>> from mastermind import db
    # >>> db.create_all()
    # >>> from mastermind import User, Post
    # >>> user_1 = User(username='tobin', email='tobin@mpn.net', password='password')
    # >>> db.session.add(user_1)
    # >>> user_2 = User(username='tobes', email='tobes@mpn.net', password='password')
    # >>> db.session.add(user_2)
    # >>> db.session.commit()
    # user = User.query.get(1)
    # >>> user
    # User('tobin', 'tobin@mpn.net', 'default.jpg')
    # >>> user.posts
    # []
    # >>> user.id
    # 1
    
    # >>> post_1 = Post(title='First Post', content='First Post', user_id=user.id)
    # >>> post_2 = Post(title='Second Post', content='Second Post', user_id=user.id)
    # >>> db.session.add(post_1)
    # >>> db.session.add(post_2)
    # >>> db.session.commit()
    # user.posts

    # [Post('First Post', '2018-12-05 08:26:22.486874'), Post('Second Post', '2018-12-05 08:26:22.487853')]
    # >>> for post in user.posts:
    # ...     print(post.title)
    # ... 
    # First Post
    # Second Post
    # >>> post = Post.query.first()
    # >>> 
    # >>> post
    # Post('First Post', '2018-12-05 08:26:22.486874')
    # >>> post.user_id
    # 1
    # >>> post.author
    # User('tobin', 'tobin@mpn.net', 'default.jpg')
    # >>> db.drop.all()
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AttributeError: 'SQLAlchemy' object has no attribute 'drop'
    # >>> db.drop_all()
    # >>> db.create_all()
    # >>> User.query.all()
    # []
    # >>> Post.query.all()
    # []
    # >>> 