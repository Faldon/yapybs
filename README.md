Yet another python blog software - yapybs
========================================
Required for running this application
-------------------------------------
Obviously, for any web application there is some infrastructure necessary to serve it:

1.  You will need a webserver (I provide information for using Apache 2.2)
2.  You will need a database (I will stick with PostgreSQL)
3.  For a python based app, you will need, of course, Python (runs on either PYthon2 or Python3)
4.  In this how-to we will use [pip](https://pypi.python.org/pypi/pip)
5.  For installing the PostgreSQL driver we will use in this how-to through pip, we need the python and postgres 
    development libraries.
    On Debian/Ubuntu:
        
        # apt-get install libpq-dev python-dev
    On RHEL/CentOS:
        
        # yum install python-devel postgresql-devel
6.  For Apache we need the wsgi module
    On Debian/Ubuntu:
        
        # apt-get install libapache2-mod-wsgi
    On RHEL/CentOS:
        
        # yum install mod_wsgi
        
How to setup your production environment
----------------------------------------
1.  Download the archive file or checkout from git:

        $ git clone http://git.thesecretgamer.de/faldon/yapybs.git /your/production/directory
    or
        
        $ git clone https://github.com/Faldon/yapybs.git /your/production/directory
        
2.  It's recommended to setup a virtual environment. Consult the python documentation how to do this.
3.  Install the requirements django, django-summernote and psycopg2.
        
        # cd /your/production/directory
        # pip install -r requirements.txt
4.  Create a production settings file by copying the provided example
        
        $ cp /your/production/directory/yapybs/production.py.example /your/production/directory/yapybs/production.py
5.  Create secret key and paste it as value for SECRET_KEY in the production setting:
        
        $ python -c /your/production/directory/create_secret.py
6.  Adjust all other settings to reflect your environment according to the comments in the production.py file.
    Mainly, provide a valid database setup
7.  For Apache 2.2, copy the provided yapybs.conf.example to the config directory of apache.

     + Debian-based: /etc/apache2/sites-available/
    
     + RedHat-based: /etc/httpd/conf.d/
    
    Adjust the vhost config to your needs according to the comments in the yapybs.conf.example file.
8.  Let django migrate the database and copy the static files. Run from your production directory:
        
        $ python manage.py migrate admin --settings=yapybs.production
        $ python manage.py migrate --settings=yapybs.production
        $ python manage.py collectstatic --settings=yapybs.production
9.  Let django run a final check:
        
        $ python manage.py check --deploy --settings=yapybs.production
    Ignore security.W019 for I think we need it for summernote.
10. Finally, it looks that you are ready to go. Restart your webserver.