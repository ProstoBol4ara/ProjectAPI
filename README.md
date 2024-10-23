# Project API

## Введение
Индивидуальный проект по теме: Создание приложения, которое позволяет пользователям смотреть фильмы, сериалы, документальные фильмы через интернет, возможно с подпиской или оплатой за просмотр

Для использования продукта требуется Docker/docker-compose.

### Для запуска с помощью docker-compose:

1) Перейдите в папку Docker/docker-compose/
2) Введите в терминал: 
```bash 
docker-compose up --build
```
3) Готово! Можно открыть браузер и проверять (http://localhost:8000/docs#)

Как удалить:
1) Перейдите в папку Docker/docker-compose/
2) Введите в терминал:
```bash
docker-compose down
```
3) Готово!

### Для запуска с помощи Docker:
1) Перейдите в папку ProjectAPI
2) Введите в терминал:
```bash
sudo docker network create api_network && sudo docker build -t postgres-database -f ./Docker/postgresql/Dockerfile ./Docker/postgresql/ && sudo docker build -t api -f ./Docker/app/Dockerfile . && sudo docker run -d --name postgres-database --network api_network -p 5432:5432 postgres-database && sudo docker run -d --name api --network api_network -p 8000:8000 api 
```
3) Готово! Можно открыть браузер и проверять (http://localhost:8000/docs#)

Как удалить:
1) Введите в терминал:
```bash
sudo docker container stop api && sudo docker container stop postgres-database && sudo docker container rm api && sudo docker container rm postgres-database && sudo docker rmi api && sudo docker rmi postgres-database && sudo docker network rm api_network
```
2) Готово!