<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./curriculum-vitae.png" alt="Project logo"></a>
</p>

<h3 align="center">Curriculum Vitae API</h3>

<div align="center">

[![GitHub Watchers](https://img.shields.io/github/watchers/GustavoMagalhaess/python-curriculum-api?style=plastic&logo=appveyor)](https://github.com/GustavoMagalhaess/python-curriculum-api/watchers)
[![GitHub Issues](https://img.shields.io/github/issues/GustavoMagalhaess/python-curriculum-api?style=plastic&logo=appveyor)](https://github.com/GustavoMagalhaess/python-curriculum-api/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/GustavoMagalhaess/python-curriculum-api?style=plastic&logo=appveyor)](https://github.com/GustavoMagalhaess/python-curriculum-api/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/GustavoMagalhaess/python-curriculum-api?style=plastic&logo=appveyor)](https://github.com/GustavoMagalhaess/python-curriculum-api/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/GustavoMagalhaess/python-curriculum-api?style=plastic&logo=appveyor)](https://github.com/GustavoMagalhaess/python-curriculum-api/pulls)

</div>

---

<p align="center"> This is a simple Flask API that provides professional career information.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The purpose of this project is provide a Curriculum Vitae API with a professional career information.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

If you intend to use docker you can just follow the steps below:

```
# Insite the project folder
$ docker build -t my-python-app .

$ docker run -it --rm --name my-running-app my-python-app

# Inside the container
$ cd database
~/database $ python create_database_exemple.py
~/database $ python insert_data_exemple.py
```

But if you intend to use python environment you must follow the steps below:

```
# Insite the project folder
$ python -m venv venv/

$ source venv/bin/activate

$ pip install requirements.txt

$ cd database
~/database $ python create_database_exemple.py
~/database $ python insert_data_exemple.py

$ python app.py # Starts your app
```

## 🎈 Usage <a name="usage"></a>

Insite the projetc you can find a postman config file with all the requests allowed (~/docs/postman_collection.json)

## ⛏️ Built Using <a name = "built_using"></a>

- [Phyton 3](https://www.python.org/) - Core
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - ORM
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) - Access Token
- [Sqlite 3](https://www.sqlite.org/) - Database

## ✍️ Authors <a name = "authors"></a>

- [@GustavoMagalhaess](https://github.com/GustavoMagalhaess) - Idea & Initial work