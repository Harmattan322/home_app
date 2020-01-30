Запуск приложения

1) `docker-compose up -d postgres`
2) `docker-compose run api migrate`
3) `docker-compose run api createsuperuser` (указываете пользователя и пароль, которого хотите создать)
4) `docker-compose up -d api`

После этого можно отправлять запрос на /api/auth, в теле JSON в котором логин и пароль :
`{"username": "", "password": ""}`.
В ответ сервер вернет токен и другую инфу.
