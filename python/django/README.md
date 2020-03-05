## Django

Using Windows 10, Git Bash, Python 3.8.0, Django 3.0.3

### Getting started

From root directory (using bash):

```
python -m venv env
source ./env/Scripts/activate
pip install django

mkdir src && cd src
django-admin.py startproject mysite .

python manage.py runserver
```

### Setting up admin account

From a new bash session (different than the one running the server):

```
python manage.py migrate
winpty python manage.py createsuperuser
```

Note: The winpty makes the Git Bash terminal act more like a real bash terminal for interacting with the console.

Django admin area localhost:8000/admin

### Building web pages

- Create a Django "app": `python manage.py startapp pages`
- Create a `urls.py` file in the `pages` directory
- Copy `mysite/urls.py` code into `pages/urls.py`, remove admin-related stuff:
- ```
  from django.contrib import admin
  from django.urls import path
  ```

urlpatterns = [
path('admin/', admin.site.urls),
]

```
- Edit `mysite/settings.py` to add `'pages'` to the end of the `INSTALLED_APPS` list

### Views
Create some Django views by editing `pages/views.py`:
```

def home(request):
return render(request, "home.html", {})

def about(request):
return render(request, "about.html", {})

```

### Templates
Create `pages/templates` directory

Create `pages/templates/home.html` and `pages/templates/about.html`
```

### URLS

Import views into `pages/urls.py`: `from . import views`

Add views to `pages/urls.py` `urlpatterns` list:

```
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about/"),
]
```

Import include in `mysite/urls.py`: `from django.urls import include`

Add views to `mysite/urls.py` `urlpatterns` list:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
]
```

### More URLs

`<a href="{% url 'home' %}">Home</a>`

### Extends base file
Create a base template in pages/templates, e.g. `pages/templates/base.html`

Make "blocks" in the base file that other pages extending the base template can insert their own content into. e.g.:
**base.html:**
```
<!DOCTYPE html>
<html lang="en">

  <head>
    <title>{% block title %}Hello, world!{% endblock %}</title>
  </head>

  <body>
    {% block content %} {% endblock %}
  </body>
  
</html>
```
**about.html:**
```
{% extends 'base.html' %}

{% block title %}About{% endblock %}

{% block content%}
<a href="{% url 'home' %}">Home</a> |
<a href="{% url 'about' %}">About</a>
<br />
ABOUT
{% endblock %}
```

### Bootstrap
Starter template (can use for base.html): https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template

Navbar: https://getbootstrap.com/docs/4.4/components/navbar/

Other components: https://getbootstrap.com/docs/4.4/components/


### Using "Python" directly in HTML page
```{% if 2 > 1 %}
Hello!
{% else %}
Goodbye!
{% endif %}
```

### Passing Python variables into HTML page
In `views.py`, before returning the render object, create a variable
and give it a value, then pass the variable in within the dictionary
in the render function call. Then to use it within the HTML page, 
wrap the variable name (that you called it in the dictionary) in `{{ }}`. e.g.:
**Within pages/views.py:**
```
def about(request):
    my_name = "Hello, My Name Is Billy Garrison"
    return render(request, "about.html", {"variable_name": my_name})
```
**Within pages/about.html:**
```
{{ variable_name }}
```

### Using external Python programs within an HTML page
In the tutorial we create a Python file in the `pages` directory, `namer.py`.
I'm not sure where else it can be created Within `namer.py`, we have a simple function:
```
def namer():
    return "My Name Is Still Billy Garrison"
```
To use this function in our `about.html` page, we need to import it into our
`about` view (in `views.py`), and call the function when we render the HTML:
```
def about(request):
    from pages.namer import namer
    return render(request, "about.html", {"my_variable": namer()})
```
Within `about.html`, we call the variable the same way we did before:
```
{{ variable_name }}
```

### Static images
Create a directory in `src` (top level folder for project, the one that contains
`mysite` and `pages`): `src/static`

Create an `images` directory inside of `src/static`

Edit `mysite/settings.py`, scroll to bottom below `STATIC = '/static/'`
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

After `{% extends 'base.html' %}`, add `{% load static %}` to be able
to reference static images, then include `<img src="{% static 'images/headshot.jpg' %}">` to use the image.

# Other static files
You can include css, js, etc. using the same method as above

### Bootstrap Cards
Cards: https://getbootstrap.com/docs/4.4/components/card/
