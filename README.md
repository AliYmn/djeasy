# Compatibility

* Django 1.8+
* Python 3.x + 
* Distribution : Debian Derivatives

# **Installations**


    sudo apt-get install python-pip
    sudo apt-get install python3-pip
    sudo apt-get install virtualenv

# Package

    pip3 install djeasy



# Configuration

* Do not forget to add the Requirements.txt file.


Example Project ;

    DjangoProject 
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
    requirements.txt ---> Add!!

Example requirements.txt : https://goo.gl/0Y9yCB

* Do not forget to add the **requirements.txt**file.

* Django Settings.py ALLOWED_HOSTS = []  server ip or domain add.

# DjEasy

    djeasy
 
 Output :

    --create                      Create a new site.
    --nginx                       Nginx restart
    Project_name --gunicorn       Gunicorn restart


# Site Publishing Steps

* Creating a virtual environment.

Follow the steps in turn.

    cd /home/
    virtualenv -p python3 DjangoEnv

* Upload your app.

We can create a copy of the project you wrote with Django.

Example :

    cd /home/
    git clone https://github.com/AliYmn/aliyaman.org
    mv aliyaman.org DjangoBlog

* Let's run the package.

We'll finish the process in four steps.

    djeasy --create
 
 ***
 
 <img src="http://i.hizliresim.com/nRG4GN.png"/>

   

