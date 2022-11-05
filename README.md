# Telegram Forwarder

## What is it?
There are some cases when you need to forward all messages from one chat in Telegram to another one.

### For example:
- You change account
- Need to share your library
- Your friend accidentally deleted your chat, but only on his side and wants to restore all history, pictures, files etc.

You can forward all messages manually. But Telegram allows to do it by 100 messages per time, and it's too long.

This script will do it automatically 100 messages per minute.

### How to use

1) Clone the repository
2) Run `pipenv install`
3) Visit https://my.telegram.org/apps and get `API_ID` and `API_HASH`
4) Paste them into variables `API_ID` and `API_HASH`
5) Replace `FROM_CHAT` and `TO_CHAT` to phone numbers you need to forward to
6) Run application and follow instructions


## Что это?
Бывают случаи, когда вам нужно переслать все сообщения из одного чата Telegram в другой.

### Например:
- Вы меняете учетную запись
- Нужно поделиться своей библиотекой
- Ваш друг случайно удалил ваш чат, но только на своей стороне и хочет восстановить всю историю, картинки, файлы и т.д.

Вы можете переслать все сообщения вручную. Но Telegram позволяет делать это по 100 сообщений за раз, а это слишком долго.

Этот скрипт будет делать это автоматически 100 сообщений в минуту.

### Как использовать

1) Клонируйте репозиторий
2) Запустите `pipenv install`
3) Посетите https://my.telegram.org/apps и получите `API_ID` и `API_HASH`
4) Вставьте их в переменные `API_ID` и `API_HASH`
5) Замените `FROM_CHAT` и `TO_CHAT` на соответствующие номера телефонов
6) Запустите приложение и следуйте инструкциям
