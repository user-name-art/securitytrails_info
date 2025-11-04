# Скрипт для работы с securitytrails.com без VPN.

### Установка

Клонируйте репозиторий в нужную директорию (если дружите с git):

```
git clone https://github.com/user-name-art/securitytrails_info.git
```

Или просто скачайте файлы requirements.txt, main.py, .env.template.

git clone удобнее с той точки зрения, что можно будет обновиться с помощью git pull, а не скачивать файл(ы) вручную.

Я храню подобные скрпиты в /home/username/scripts

Запустите консоль и перейдите в директорию securitytrails_info (создается при клонировании репозитория). Создайте виртуальное окружение: 

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

Для macOS может понадобиться понизить версию urllib3: 

```
pip install urllib3==1.26.15
```

Переименуйте .env.template в .env, откройте его и измените API-ключ на свой (получить можно на securitytrails.com, для этого нужно зарегистрироваться, на почту gmail регистрирует нормально). По API с одним ключом можно сделать 50 запросов в месяц, счетчик сбрасывается в первый день нового месяца.

![0](https://github.com/user-attachments/assets/a14bb112-8594-40c9-83d8-e094c9524656)

Создайте алиас в .bashrc (или в .zshrc):

```
alias sec="/home/username/scripts/securitytrails_info/.venv/bin/python /home/username/scripts/securitytrails_info/main.py"
```

* sec - это название команды, с помощью которой вы будете запускать скрипт;
* /home/username/scripts/securitytrails_info - путь к виртуальному окружению;
* .venv - директория виртуального окружения 
* /home/username/scripts/securitytrails_info/main.py - путь к скрипту.

### Работа со скриптом

![00](https://github.com/user-attachments/assets/b978eb44-16cc-43b1-9e8d-b73ffb04b34e)

Скрипт умеет выводить только историю ресурсных записей A, NS, MX или TXT для указанного домена. По умолчанию без указания дополнительных аргументов выводится история по записям A.

```
sec oracle.com
```

Имя домена нужно передавать в аргументах без http/https и слэшей. Возможно, в дальнейшем появится "очистка" от протоколов и слэшей, но пока этого нет.

Посмотреть историю записей NS:

```
sec oracle.com ns
```

Записей MX:

```
sec oracle.com mx
```

И записей TXT:

```
sec oracle.com txt
```

Другие записи пока не поддерживаются. Не уверен, что они нужны, но если вдруг надо - пишите. 

Показать справку и версию скрипта:

```
sec -h
```
