# Скрипт для работы с securitytrails.com без VPN.

### Установка

Клонируйте репозиторий в нужную директорию (если дружите с git):

```
git clone https://github.com/user-name-art/securitytrails_info.git
```

Или просто скачайте файлы requirements.txt, main.py, .env.template.

git clone удобнее с той точки зрения, что можно будет обновиться с помощью git pull, а не скачивать файл(ы) вручную.

Я храню подобные скрпиты в /home/username/scripts

Запустите консоль и перейдите в директорию securitytrails_info. Создайте виртуальное окружение: 

```
python -m venv .venv
```

Активируйте его: 

```
source .venv/bin/activate
```

Установите необходимые зависимости: 

```
pip install -r requirements.txt
```

Переименуйте .env.template в .env, откройте его и измените API-ключ на свой (получить можно на securitytrails.com, для этого нужно зарегистрироваться, на почту gmail регистрирует нормально).

Создайте алиас в .bashrc (или в .zshrc):

```
alias sec="/home/username/scripts/securitytrails_info/.venv/bin/python /home/username/scripts/securitytrails_info/main.py"
```

* sec - это название команды, с помощью которой вы будете запускать скрипт;
* /home/username/scripts/securitytrails_info - путь к виртуальному окружению;
* .venv - директория виртуального окружения 
* /home/username/scripts/securitytrails_info/main.py - путь к скрипту.

### Работа со скриптом

![photo_2024-10-22_10-54-40](https://github.com/user-attachments/assets/e60fde36-2f79-4ecf-890f-f7a9e46795d3)

Пока что скрипт может выводить только историю IP-адресов для указанного домена. 

```
sec oracle.com
```

Имя домена передаем в аргументах без http/https. Возможно, в дальнейшем появится "очистка" от протоколов и слэшей, но пока этого нет.
