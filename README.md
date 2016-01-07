# my-first-django-tutorial
This is the code for a tutorial I created about Django for beginners, with special focus on Windows.<br/>
You can find this tutorial and more like it on my personal website http://lanigouws.com

<h5>To make it work</h5>

- You need to create a virtualenv with:<br/>
  <code>mkvirtualenv name</code>
- Then install the required packages, into the virtualenv, with:<br/>
  <code>pip install -r requirements.txt</code>
- Add a SECRET_KEY in <strong>settings.py</strong>
- Then <code>python manage.py migrate</code>
- Create a superuser for the admin site: <code>python manage.py createsuperuser</code>
- And <code>python manage.py runserver</code> to activate the development server.
