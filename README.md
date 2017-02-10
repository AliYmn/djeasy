# Compatibility

* Django 1.8+
* Python 3.x + 
* Distribution : Debian Derivatives

# **Installations**


    sudo apt-get install python-pip
    sudo apt-get install python3-pip

# Package

    pip3 install git+https://github.com/AliYmn/djeasy



# Configuration

* Do not forget to add the Requirements.txt file.


Example Project ;

    DjangoProject  --> move to /home/ Add!
    ├── DjangoProject
    │   ├── __init__.py
    │   ├── settings.py
    │   └── urls.py
    │   └── wsgi.py
    ├── Blog
    │    ├── __init__.py
    │    └── admin.py
    │    └── apps.py
    │    └── tests.py
    │    └── views.py
    requirements.txt ---> Add!

Example requirements.txt : https://goo.gl/0Y9yCB

* Move the file named Django Project to **/home/** directory 

* Django Settings.py ALLOWED_HOSTS = []  server ip or domain add.

# DjEasy

We are starting now! :)

    djeasy
 
 Output :

<img src="http://image.prntscr.com/image/c89f074de20b43f3a9532033ff844c27.png"/>

    Options:
      --create                 A new site
      --collectstatic          static file
      --makemigrations         database makemigrations
      --migrate                database migrate


# DjEasy Create Site

    djeasy --create
   
Output :
    
 <img src="http://image.prntscr.com/image/3f7c4755b4c145d8ab4e1b5cada271e4.png"/>
 It's so easy :)
 
 
* Warning : Make sure you are entering the correct information.

# Congratulations Successful!

<img src="http://image.prntscr.com/image/fe6e3dd4bb2c4454a3f202d5f2b8fda9.png"/>

# Create the PostgreSQL Database and User

 https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-the-postgresql-database-and-user
    
