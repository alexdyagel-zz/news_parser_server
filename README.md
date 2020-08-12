# Feed parser server
It is server which scans the sources of rss news and stores them in database.
You can get access to them using api requests.
### Installation
Install required packages using requirements file:
```sh
$ pip install -r /path/to/requirements.txt
```
Also you should create .env file with the following variables:
```
POSTGRES_ADDRESS=news-database
POSTGRES_PORT=5432
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
APP_PORT=8023
```
POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD specify on your own.

In config.json please specify urls with rss which you want to parse.

### Run Feed Parser

You can run it with the help of simple command

```sh
$ docker-compose up
```

After launch you can get all news through request:

```sh
http://0.0.0.0:8023/news
```
or you can get access to news on the specified date:
```sh
http://0.0.0.0:8023/news/date=2020/08/11
```

Enjoy it!