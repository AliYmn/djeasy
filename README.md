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
    
 