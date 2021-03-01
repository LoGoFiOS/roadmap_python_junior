## Создание виртуального окружения

```bash
# создание папки venv с виртуальным окружением
python3 -m venv venv
# Переходим в виртуальную среду
source venv/bin/activate
# Установка пакетов
pip install -r requirements.txt
# выходим из виртуальной среды
deactivate
```

## Настройка сервера

```bash
# Обновление
apt update
apt upgrade
# МБ нужна установка
apt install python3-venv
```



## Работа с Docker

### Общее

```bash
# установка
apt install docker docker-compose

# Просмотр, остановка и удаление контейнеров
docker ps
docker kill [name]
docker rm [name]

# Просмотр и удаление образов
docker images
docker rmi [id]

#  Войти в контейнер

# Перезапуск демона Docker со всеми контейнерами
systemctl enable docker.service

```

### Пример запуска postgreSQL

```bash
# Остановть, если есть работающая база
systemctl stop postgresql

# Запуск контейнера с Potgresql
docker run --name [container_name] -e POSTGRES_PASSWORD=[pass] -e POSTGRES_USER=[user] -e POSTGRES_DB=[db] -p [5432:5432] -d postgres

#  Войти в контейнер и БД
# --dname, если названия user != db
docker exec -it [container_name] psql -U [postgres_user] --dbname [db]

```

### Работа с Docker compose

```bash
# Войти в контейнер. Например, это МБ Postgres
docker-compose run [service_name] bash

# Подкючиться к базе. Host из Docker - название контейнера в Docker-compose
psql --host=[host] --username=[user] --dbname=[database_name]

# Остановить и удалить образы
docker-compose down

```





## Работа с Git

```bash
# создание репозитория

```

