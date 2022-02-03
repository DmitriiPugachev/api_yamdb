### Description:
API for YaMDb.
#### You can:
  * create new users;
  * get, create, update and delete users;
  * get and update data your personal userdata;
  * get, create and delete categories;
  * get, create and delete genres;
  * get, create, update and delete title data;
  * get, create, update and delete reviews;
  * get, create, update and delete comments.
#### Techs:
  * requests==2.26.0
  * django==2.2.16
  * djangorestframework==3.12.4
  * djangorestframework-simplejwt=4.3.0
  * pytest==6.2.4
  * pytest-django==4.4.0
  * python-dotenv==0.13.0
  * pytest-pythonpath==0.7.3
  * django-filter=21.1
  * PyJWT==1.7.1
  * sqlparse==0.3.1
### How to run the project local:
Clone a repo and go to its directory:
```bash
git clone https://github.com/DmitriiPugachev/api_yamdb.git
```
```bash
cd api_yamdb
```
Create and activate virtual environment:
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
Install and upgrade pip:
```bash
python3 -m pip install --upgrade pip
```
Install all the dependencies from a ```requirements.txt``` file:
```bash
pip install -r requirements.txt
```
Create a ```.env``` file in the root directory and fulfill it like ```.env.example```.

Migrate:
```bash
python3 manage.py migrate
```
Run the project:
```bash
python3 manage.py runserver
```
### Links
[redoc with all possible request examples](http://127.0.0.1:8000/redoc/) this link is for local usage.
### Authors
Dmitrii Pugachev

Mariya Yaschuk

Alexandr Klimenko
