# Data4Good Django on Amazon Web Services (Elastic Beanstalk)

[![Build Status](https://travis-ci.com/d4gumich/data4good-django.svg?branch=master)](https://travis-ci.com/d4gumich/data4good-django)
[![Known Vulnerabilities](https://snyk.io/test/github/d4gumich/data4good-django/badge.svg)](https://snyk.io/test/github/d4gumich/data4good-django)
![GitHub repo size](https://img.shields.io/github/repo-size/d4gumich/data4good-django.svg)
![GitHub](https://img.shields.io/github/license/d4gumich/data4good-django.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/d4gumich/data4good-django.svg)
![](https://img.shields.io/badge/django-✓-blue.svg)
![](https://img.shields.io/badge/semantic_uI-✓-blue.svg)
![](https://img.shields.io/badge/aws_elastic_beanstalk-✓-blueviolet.svg)

[Website](http://data4good.fjwji7zqan.us-east-1.elasticbeanstalk.com/)


## Project Layout
| Key Folder | Parent Folder | Description |
| - | - | - |
| d4g | d4g | Holds the settings.py and root urls | 
| home | home/templates/ | Holds the root HTML that has the style | 
| web | d4g| Holds all the templates and python files for website | 


## Development

This project is built with [Django](https://www.djangoproject.com/) on [AWS Beanstalk](https://aws.amazon.com/elasticbeanstalk/). Database solution is [PostGresql, look at this guide for installation with Django](https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989)


## Setup

### Django
Activate the virtual environment
```
source ~/eb-virt/bin/activate
```

Install the requirements from the requirements.txt
```
pip install -r requirements.txt
```

Run the server and look at the localhost
```
python manage.py runserver
```

### AWS + Beanstalk

- Get Django working on AWS by [installing the Elastic beanstalk CLI](https://github.com/aws/aws-elastic-beanstalk-cli-setup).
- Run `eb init` inside a directory

Then to get eb in your system path
```
 echo 'export PATH="/Users/[YOUR-USERNAME]/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```

## Deploy on AWS + Beanstalk
find the domain name of your new environment by running 
 
```
eb status
```

Activate the virtual environment
```
source ~/eb-virt/bin/activate
```

Commit your files to git before you deploy them to AWS
```
git commit .
```

Deploy
``` 
eb deploy data4good-env
```

Open the project on the web!
``` 
eb open data4good-env
```

## Run Locally
Just activate your virtual environment and run

```
source ~/eb-virt/bin/activate
```

```
python manage.py runserver
```

## Troubleshooting
- https://stackoverflow.com/questions/58373960/wsgi-error-using-django-2-2-on-elastic-beanstalk
- https://github.com/jiansoung/issues-list/issues/13
- [Deploying Django + Python 3 + PostgreSQL to AWS Elastic Beanstalk](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)

# Key Libraries
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>

![Semantic](http://semantic-ui.com/images/logo.png)
