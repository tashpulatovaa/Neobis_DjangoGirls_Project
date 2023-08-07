# Neobis_DjangoGirls_Project

This is a simple django girls project with list of blogs with create post function.

## Requirements

* Python 3.x
* Django 3.x

## Installation
1. Clone the repository to your local machine:
 ```
git clone https://github.com/tashpulatovaa/Neobis_DjangoGirls_Project.git
  ```

Steps and commands for Linux machine are the same but use python3 instead of python.

2. Create and activate a virtual environment (optional but recommended):
 ```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:
```
cd Neobis_DjangoGirls_Project/django_girls
pip install -r requirements.txt
```
4. Apply migration to setup the database:
```
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```
6. Open your web browser and navigate to http://localhost:8000/ to access the Todo app.

## Usage

* #### create_post:
On the main page, find the "Create post" button, enter the title, content, author, slug and status to create a new post.
* #### List of post:
On the main page, there are list of posts, you can read full version by clicking on "Read more" button


## File Structure
* ##### django_girls/models.py:
  Defines the django_girls model for tasks.
* ##### django_girls/views.py:
  Contains the views for handling different read more, create post functioins
* ##### django_girls/blog/templates
* Lit of pages that are rendered on each url path
* ##### ToDo/urls.py:
  Contains URL patterns for mapping views to URLs.



