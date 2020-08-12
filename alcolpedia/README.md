# alcolpedia

<div class = "shields" style = "display: flex; "> 
    <img src = "https://img.shields.io/github/issues/rlwjd4177/alcolpedia">
    <img src = "https://img.shields.io/github/forks/rlwjd4177/alcolpedia">
    <img src = "https://img.shields.io/github/stars/rlwjd4177/alcolpedia">
    <img src="https://img.shields.io/github/languages/top/rlwjd4177/alcolpedia" />
    <img src="https://img.shields.io/github/last-commit/rlwjd4177/alcolpedia"/>
    <img src="https://img.shields.io/github/license/rlwjd4177/alcolpedia" />
</div>

alcolpedia is a django website to introduce various drinking cultures in Korea

## Mock Up Design

- <a href = "https://ovenapp.io/view/jjqI146GVpoS9PIuzhZUiKk1TUTMNlPh#zueVT"> ovenapp.io를 이용한 Mockup design </a>
- <a href = "https://xd.adobe.com/view/77b781f7-9178-4f69-96fe-3b88d1735d95-22e4"> adobe XD를 이용한 Mockup Design </a>

## Usage

1. dowload this repository
```bash
$ git clone https://github.com/rlwjd4177/alcolpedia 
```

2. venv settings

```bash
$ cd alcolpedia
$ python -m venv venv
```

- ubuntu
```bash
$ source ./venv/bin/activate    
``` 
- Window
```bash
$ .\venv\Scripts\activate
```

3. pip install 
```bash
$ pip install -r requirements.txt
```

4. make secrets.json file
You can make secret key in django secret key generator site
(ex. <a href = "https://miniwebtool.com/django-secret-key-generator/">here</a>)
```
{
    "SECRET_KEY": "YOUR_SECRET_KEY"
}
```

5. start website server
```bash
$ cd alcolpedia
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

6. Enter http://127.0.0.1:8000/

## How to Contribute

1. fork this repository `https://github.com/rlwjd4177/alcolpedia`

2. clone your `alcolpedia` repository

3. venv settings

```bash
$ cd alcolpedia
$ python -m venv venv
```

- ubuntu
```bash
$ source ./venv/bin/activate    
``` 
- Window
```bash
$ .\venv\Scripts\activate
```

4. pip install 
```bash
$ pip install -r requirements.txt
```

5. make secrets.json file
You can make secret key in django secret key generator site
(ex. <a href = "https://miniwebtool.com/django-secret-key-generator/">here</a>)
```
{
    "SECRET_KEY": "YOUR_SECRET_KEY"
}
```

6. Write your code

7. start website server & test your code
```bash
$ cd alcolpedia
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

8. change your git branch and commit, push
```
$ git checkout develop
$ git add YOUR_CODE_FILE
$ git commit -m "YOUR_COMMIT_MESSAGE"
$ git push origin develop
```

9. go to your repository & send pull request

## How to Synchronize origin repository

1. add remote url
```
$ git remote add upstream https://github.com/ryou73/re_hanalum
```

2. fetch & merge
```
$ git fetch upstream
$ git checkout BRANCH_NANE
$ git merge upstream/master
```

3.  reflect in your remote repository
$ git push origin master

## LICENSE
