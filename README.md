# Проект-пример Django-docker-example

## Что умеет приложение? 

Приложение обладает простейшим интерфейсом для загрузки файлов в базу данных.
Для запуска следуйте одной из инструкций, указанных ниже.

## Как запустить?
Создайте в директории django-example-docker одну обязательную и две необязательных переменных окружения:
1) `.env` - обязательная.

- `DEBUG`= настройка Django для включения отладочного режима. Принимает значения `TRUE` или `FALSE`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG).
- `SECRET_KEY`= обязательная секретная настройка Django. Это соль для генерации хэшей. Значение может быть любым, важно лишь, чтобы оно никому не было известно. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key).
- `ALLOWED_HOSTS`= настройка Django со списком разрешённых адресов. Если запрос прилетит на другой адрес, то сайт ответит ошибкой 400. Можно перечислить несколько адресов через запятую, например `127.0.0.1,192.168.0.1,site.test`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).
- `DATABASE_URL`= адрес для подключения к базе данных PostgreSQL. Другие СУБД сайт не поддерживает. [Формат записи](https://github.com/jacobian/dj-database-url#url-schema).
- `CSRF_COOKIE_DOMAIN`= `http://127.0.0.1:1337`, `http://mydomain.ru`, `https://mydomain.ru` [Документация](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-domain).
- `CSRF_TRUSTED_ORIGINS`= `http://127.0.0.1:1337`, `http://mydomain.ru`, `https://mydomain.ru` [Документация](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins).
- `VIRTUAL_HOST`= `http://mydomain.ru` - настройка для prod версии.
- `VIRTUAL_PORT`= `8000` - настройка для prod версии.
- `LETSENCRYPT_HOST`= `http://mydomain.ru` - настройка для prod версии.

#### ВАЖНО! В переменной `DATABASE_URL` вместо localhost используйте `host.docker.internal` если необходимо подключиться к postgres на локальном сервере.

2) `.env.db` - необязательная.

- `POSTGRES_USER`=`psql_user` - если БД должна находиться в контейнере.
- `POSTGRES_PASSWORD`=`psql_pass` - если БД должна находиться в контейнере.
- `POSTGRES_DB`=`psql_db_name` - если БД должна находиться в контейнере.

3) `.env.proxy-companion` - необязательная.

- `DEFAULT_EMAIL`= `your_email@mail.com` - настройка для prod версии. На этот адрес будут приходить уведомления от [letsencrypt.org](https://letsencrypt.org)
- `ACME_CA_URI`= `https://acme-staging-v02.api.letsencrypt.org/directory` - настройка для prod версии.
- `NGINX_PROXY_CONTAINER`= `nginx-proxy` - настройка для prod версии. Название вашего nginx-proxy контейнер из docker-compose.prod.yaml.


### Docker-compose для локального сервера
- Выполните команду:
```shell
docker-compose -f docker-compose.dev.yaml up --build -d
```
### Docker-compose для локального сервера с psql на localhost
- Выполните команду:
```shell
docker-compose -f docker-compose.local-psql.yaml up --build -d
```
### Docker-compose для dev сервера
- Выполните команду:
```shell
docker-compose -f docker-compose.prod.yaml up --build -d
```
### Docker-compose для dev сервера с psql на localhost
- Выполните команду:
```shell
docker-compose -f docker-compose.prod.local-psql.yaml up --build -d
```
### Завершить работу docker-compose
- Выполните команду:
```shell
docker-compose -f docker-compose* down -v
```
- На месте `*` - название выбранного docker-compose.    
- `-v` указывается в том случае, если необходимо удалить `volumes`.

