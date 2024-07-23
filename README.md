# Database for the school of Divinity, History, Philosophy, and Art History of the University of Aberdeen - Codename: Hotel
This repository hosts the source code for a webapp based on Django, providing users with the ability to browse through a database of visual research data.

The application can be found running on a VM provided by the University of Aberdeen at [http://137.50.202.150/](http://137.50.202.150/).
Unfortunately, we are not able to run the Virtual Machine continuously, and the application is therefore not accessible at all times until the hosting method is changed.

## Maintenance
### Code structure
The application follows the basic Django structure.

You'll find everything needed to understand how Django works in [its documentation](https://docs.djangoproject.com/en/5.0/).

Included libraries and packages include:
  - [Bootstrap](https://getbootstrap.com/) for easy CSS management
  - [Crispy](https://django-crispy-forms.readthedocs.io/en/latest/index.html) for the form CSS, has to be installed through pip along with [Crispy for Bootstrap 4](https://github.com/django-crispy-forms/crispy-bootstrap4)
  - [Openlime](https://github.com/cnr-isti-vclab/openlime) for RTI visualisation. This is contained within `/homepage/static/js` in the two .js files.
  - [Pillow](https://pillow.readthedocs.io/en/stable/) for proper handling and displaying of image files fetched from the database

### Deployment
As any Django application, the server is run in a Python environment and just requires that adjustments are made to the `djangoBackend/settings.py` file, for which [documentation is provided](https://docs.djangoproject.com/en/5.0/topics/settings/).

You will find a simple guide for deploying a Django application in [their documentation](https://docs.djangoproject.com/en/5.0/howto/deployment/).

Before running the server, you will need to install the necessary packages with the following commands:
```
pip install django
pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap4
```

If the database is refactored in any way, migrations need to be created an applied.
This is done through running the three following commands:
```
manage.py makemigrations
manage.py makemigrations homepage
manage.py migrate
```
You can then run the server with the following command:
```
manage.py runserver 0.0.0.0:80
```

The code hosted in this repository is fit for a Debian server with admin priviledges and an open HTTP port.

The firewall used is [UFW](https://help.ubuntu.com/community/UFW).

### Administration and moderation
Once the Django application is deployed, most of the administration is done through the [django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/) environment.

You can access the database and moderate it through the [django admin page](https://docs.djangoproject.com/en/5.0/#the-admin).

Uploaded items are automatically put in the main database. This is temporary and should be changed as soon as possible in two different ways:
  - a temporary "sandbox" for moderation of incoming content
  - user authentication to limit uploading to authorised users

In the mean time, logging in to the admin page provides everything needed for moderation.

## Extending the project
### Adding functionalities
There are multiple functionalities that should be added to the project:
  - as stated earlier, an authentication system, integrated with the university's system for authentication and accepting institutional login for more universities in the UK
  - more fields for details about the items: copyrights, crediting, etc.
  - more search functionalities, including but not limited to:
    - tags for items
    - collections of items
    - text similarity for authors and titles
  - handling of three-dimensional data (although this is less essential)

### Refactoring
The project is small enough in its current state that Django is sufficient.

In terms of the Django Python-based code, models, forms, and views should be changed to make the code clearer and more concise.
Functions in `views.py` that aren't meant to forward HTTP requests to the render of a template should also be moved to a separate .py file.

The templates should need minimal cleaning, but the stylesheets may need more organisation.
Bootstrap clearly need to be implemented more in order to make the UI reponsive, and to facilitate further work on it.

As the university's brand guidelines are set to change in the coming months, the UI should be updated to reflect those changes.

The upload form should be more extensive, reflecting potential changes made to the models and being clearer overall.
### Strengthening
Settings should be changed so that the website uses HTTPS instead of HTTP.

### Team
Michael Nii Nai Nai-Kwade, 

Xin Feng, 

Qiancheng Luo, 

Haichun Wang, 

Xiaofan Chen,

Valentine Akoma