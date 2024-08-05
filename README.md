We can create a todo list by logging in from the admin panel on our website and add categories and tags.


## Usage

**Preferably use `virtualenv`:**

```bash
# Create a virtual environment
virtualenv django-firm_vnv

# Activate the virtual environment
todo_vnv\Scripts\activate
pip install -r requirements.txt
# Apply the migrations to the database 
py manage.py migrate 
py manage.py createsuperuser # Follow the prompts to add an admin user
py manage.py makemigrations
py manage.py migrate
py manage.py runserver   		
```
