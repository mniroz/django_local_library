# Django Local Library

## Введение
Веб-приложение создает онлайн-каталог для небольшой местной библиотеки. Пользователи могут просматривать доступные книги и управлять своими учетными записями.

Основными функциями, которые были реализованы в настоящее время, являются:
- Имеются модели для книг, экземпляров книг, жанра, языка и авторов.
- Пользователи имеют возможность просматривать список и подробную информацию о книгах и авторах.
- Пользователи с правами администратора могут создавать модели и управлять ими. Админка сайта была оптимизирована под потребности моделей, также базовая регистрация присутствует в admin.py , но закомментирована.
- Библиотекари могут продлевать зарезервированные книги

![Database structure for the local library](https://raw.githubusercontent.com/mdn/django-locallibrary-tutorial/master/catalog/static/images/local_library_model_uml.png)

## Запуск приложения на Ubuntu 20.04
1. Настройка виртуальной среды Python (предполагается, что Python версии 3.10.6 и pip3 [уже установлены](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-ru "Установка Python 3 и настройка среды программирования на сервере Ubuntu 20.04"))
```
mkdir environments
cd environments
python3.10 -m venv my_env
source my_env/bin/activate # активируем среду, чтобы ее использовать
```
2. Выполните следующие команды:
```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py test # Run the standard tests. These should all pass.
python3 manage.py createsuperuser # Create a superuser
python3 manage.py runserver
```
3. Откройте браузер `http://127.0.0.1:8000/admin/`, чтобы попасть на сайт администратора
4. Создайте несколько тестовых объектов каждого типа
5. Откройте вкладку с адресом `http://127.0.0.1:8000`, чтобы увидеть основной сайт с новыми объектами, которые вы добавили на предыдущем шаге
