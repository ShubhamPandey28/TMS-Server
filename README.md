# TMS-Server
Backend system of Transport-Management-System

## Using api

clone TMS-Server 

```bash
git clone https://github.com/ShubhamPandey28/TMS-Server.git
```

it is adviced to use a virtualenv. You can use pipenv install it using pip<br>
```bash 
pip install --upgrade pipenv
```

To activate virtualenv just do following
```bash
cd TMS-Server
pipenv shell
```

install the dependencies

```bash
pip install -r requirements.txt
```

setup the mysql database by running <br>
```bash
python dbsetup.py
``` 


Then finally run the server <br>
```bash
python app.py
```

api-url is ```http://127.0.0.1:5000/```
