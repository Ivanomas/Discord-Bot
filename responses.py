import random
import requests


# Функция, которая передаёт сообщение, которое отправляет бот в зависимости от того, что написал пользователь
def get_response(message):
    # Для начала приведём сообщение пользователя в один регистр для удобства
    # Также для некоторых ответов предусмотрены сразу несколько сообщений пользователя. Например, если пользователь
    # напишет hello, то получит один и тот же ответ, который получил бы, если написал helo (с ошибкой)
    p_message = message.lower()
    if p_message == 'hello' or p_message == 'helo':
        return 'Hello! You can use "help" to know my commands'
    if p_message == 'help':
        return 'I have these commands:help, math, python, cat and dog. I can also use dms if you type command with "!"' \
               '\n others are not implemented yet'
    if p_message == 'python' or p_message == 'programming' or p_message == 'programmer':
        return 'You want to be a programmer? Be sure to check python on https://python.org'
    if p_message == 'roll':
        # Возвращает случайное число от 1 до 10
        return random.randint(1, 10)
    # Если строчка начинается с math, то бот считает выражение и выдаёт ответ
    if p_message[:4] == 'math':
        p_message = p_message[4:]
        if p_message.isalpha():
            return 'I cannot get the answer because this is not countable'
        if p_message[1:].isalpha():
            return 'I cannot get the answer because this is not countable'
        return f'The answer is: {eval(p_message)}'
    if 'cat' in p_message:
        # Cat и dog возвращают ссылку на картинку, которая открывается отдельно в браузере
        return (requests.get('https://api.thecatapi.com/v1/images/search')).json()
    if 'dog' in p_message:
        return (requests.get('https://dog.ceo/api/breeds/image/random')).json()
    # В случае, когда ни одно сообщение не предусмотрено ботом, он возвращает небольшое сообщение, а также возвращает
    # сообщение пользователя, будучи его эхом
    return f'Sorry, but I can not understand your request, I can be your echo for a while!' \
           f'\n I can be your echo, though!' \
           f'\n {message}'
