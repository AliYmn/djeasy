# DjEasy 🎵

[![PyPI version](https://img.shields.io/pypi/v/djeasy.svg)](https://pypi.org/project/djeasy/)
[![License](https://img.shields.io/pypi/l/djeasy.svg)](https://github.com/AliYmn/djeasy/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/djeasy)](https://pepy.tech/project/djeasy)
[![Forks](https://img.shields.io/github/forks/AliYmn/djeasy.svg?style=social&label=Fork)](https://github.com/AliYmn/djeasy/fork)
[![Stars](https://img.shields.io/github/stars/AliYmn/djeasy.svg?style=social&label=Star)](https://github.com/AliYmn/djeasy/stargazers)
[![Contributors](https://img.shields.io/github/contributors/AliYmn/djeasy.svg)](https://github.com/AliYmn/djeasy/graphs/contributors)

Welcome to DjEasy, your go-to tool for simplifying Django project deployments without docker etc.

## Compatibility

- **Django**: 1.8+
- **Python**: 3.x +, 2.x +
- **Supported OS**: Ubuntu (Debian Derivatives), CentOS (coming soon)

## Installation 🛠️

Ensure you have the following installed:

    sudo apt-get install python-pip
    sudo apt-get install python3-pip
    sudo apt-get install virtualenv

# Package

    pip install djeasy
    #or
    pip3 install djeasy

# Configuration
This is important this project. Because your project doesn't match this directory doesn't work.
* You must add <b>requirements.txt</b>

# Example Project ;

    DjangoBlog
    ├── DjangoBlog
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

* Do not forget to add the **requirements.txt** file.

* Django Settings.py **ALLOWED_HOSTS = []**  server ip or domain add.

# DjEasy

    djeasy

 Output :

    --create                      Create a new site.
    --nginx                       Nginx restart

# Site Publishing Steps

* You must create virtualenv for your project and this package.
* NOT : You should know virtualenv name to use djeasy.

You can follow this;

    cd /home/ # as you wish. My recommended in your /home/ directory.

    virtualenv -p python3 DjangoEnv # example name : DjangoEnv

* Upload or clone your project in server directory like /home/


Example :

    cd /home/
    git clone https://github.com/AliYmn/aliyaman.org
    mv aliyaman.org DjangoBlog # to change name

* Let's run the package.

We'll finish the process in four steps.

    djeasy --create

 ***

* You can give any name you want for nginx and gunicorn name. But you should don't keep in mind names, because you'll use this for restart nginx and gunicorn.

 <img src="https://github.com/AliYmn/djeasy/raw/master/images/ex3.png"/>

NOT : You can write multiple site. For example, example1.com example2.com

Example;

    server ip or domain = 192.241.163.191 example.com blog.example.com
***

* Restart the server

Commands used ;

    --nginx                        Nginx restart
    gunicorn_name --gunicorn       Gunicorn restart

Example;

    djeasy --nginx
    djeasy DjangoBlog --gunicorn

Output;

 <img src="https://github.com/AliYmn/djeasy/raw/master/images/ex2.png"/>

# Process completed successfully.

 <img src="https://github.com/AliYmn/djeasy/raw/master/images/ex1.png"/>

NOT : The Json file is saved in the home directory, please do not delete it.
