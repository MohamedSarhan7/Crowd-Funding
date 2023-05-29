# Crowd-Funding

Crowdfunding is the practice of funding a project or venture by raising small
amounts of money from a large number of people, typically via the Internet.
Crowdfunding is a form of crowdsourcing and alternative finance.

## Run Locally

<hr>
Postman

Check out [API Postman Collection](https://api.postman.com/collections/19873401-6a3e335f-0f08-4235-a582-38463d019daf?access_key=PMAT-01H1JGTXHZN40X4PX4FW9F1ADM){:target="_blank"}.
<hr>
Clone the project

```bash
  git clone git@github.com:MohamedSarhan7/Crowd-Funding.git
```
<hr>

### create virtual environment 

### windows 
* create 
```bash
  python -m venv env
```
* activate
```bash
  env\Scripts\activate
```

### ubuntu 
* install venv 
```bash
sudo apt-get install python3-venv

```
* create 
```bash
python3 -m venv env
```
* activate
```bash
  source env/bin/activate
```
<hr>

Go to the project directory

```bash
  cd Crowd-Funding
```

Install dependencies

```bash
  pip install -r requirements.txt
```

create .env file

> :warning:
> **please don't forget to fill the env variables**

```bash
  cp .env.example .env
```

make migrations

```bash
  python manage.py makemigrations customauth
  python manage.py makemigrations api
```

migrate

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```
