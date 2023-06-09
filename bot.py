import discord
import responses


# Основная функция для отправки сообщения, зависит от сообщения пользователя и is_private, которая показывает, хочет
# пользователь отправить сообщение ему в личные сообщения, или в канал бота
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    # В случае ошибки бот выводит ошибку в консоль, ничего не делая в самом канале
    except Exception as e:
        print(e)


# Нерабочая функция, которая будет доработана в будущем. Должна будет выводить всех пользователей на сервере
async def server_list(message, us_message, is_private):
    try:
        members = 'test'
        await message.author.send(members) if is_private else await message.channel.send(members)

    except Exception as e:
        print(e)


# Когда пользователь присоединяется, он пишет ему в личные сообщения приветствие
async def on_member_join(member):
    try:
        await member.create_dm()
        await member.dm_channel.send(f'Hello, {member.name}')

    except Exception as e:
        print(e)


# Непосредственно сам бот, который запускает бота в чате
def run_bot():
    # Индивидуальный токен, который выдаёт сам дискорд
    TOKEN = 'MTA5OTQwMTg2MzAzMzUzMjU3Nw.GE7Dqv.flmXg16Lc7WEsIIqZ6GAEE24LjvlHz--3HWxKo'
    # Определение намерений бота, конкретно есть guilds и message_content
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.invites = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        # Функция, которая пишет в консоль сообщение, когда бот запустился
        print("Hey, bot is working now")

    @client.event
    # Функция, которая должна писать айди приглашения при его создании, сейчас не работает, будет доработано
    async def on_invite_create(invite):
        print(client.invite.id)

    @client.event
    async def on_message(message):
        # Основная функция, которая запускается при сообщении
        if message.author == client.user:
            # Необходимая строчка, которая делает так, чтобы бот не реагировал на самого себя
            return
        # Определение автора сообщения, его сообщения и канала, где он что-либо написал
        username = str(message.author)
        us_message = str(message.content)
        channel = str(message.channel)
        # Логирование в консоль всего, что говорят на сервере. Реагирует на абсолютно всех каналах
        print(f'{username} said {us_message} on {channel}')

        # Проверка на то, что пользователь пишет в отдельный текстовый канал под названием "bot". Сделано для того,
        # чтобы он не реагировал на, например, обычные разговоры в канале, когда помощь бота не нужна
        if channel == 'bot':
            if us_message[0] == '!':
                # Проверка начала сообщения. Если оно начинается с "!", то для начала обрезается строчка для удобства
                # Потом is_private ставится на True, из-за чего бот пишет в личные сообщения, в противном случае -
                # пишет в сам канал бота. Обащается к функции send_message
                us_message = us_message[1:]
                await send_message(message, us_message, is_private=True)
            else:
                await send_message(message, us_message, is_private=False)

    client.run(TOKEN)
