# Cервис управления рассылками, администрирования и получения статистики 

## Краткое описание
Адаптивный сервис рассылки, который создан с использованием BOOTSTRAP и Django.

## Описание
* Интерфейс системы содержит следующие экраны:список рассылок, отчет проведенных рассылок отдельно, создание рассылки,
  удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
* При создании рассылки создается задача с периодическими рассылками.
* Реализовано приложение для ведения блога.
* Права доступа разделены для различных пользователей.

_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_

_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для заполнения БД запустить команду:_

```
python3 manage.py fill
```

_Для создания администратора запустить команду:_

```
python3 manage.py csu
```

_Для запуска redis_:

```
redis-cli
```

_Для запуска приложения:_

```
python3 manage.py runserver
```