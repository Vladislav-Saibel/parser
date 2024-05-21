from telethon import TelegramClient, events


def telegram_parser(send_message_func=None, loop=None):
    '''Телеграм парсер'''

    # Параметры из my.telegram.org
    api_id = 26427761
    api_hash = '6d160a6667d27e2fcf509a0d993a5a82'
    # Канал источник новостей @prime1
    channel_source = 'https://t.me/vlad_chatbot'

    # Сессия клиента telethon
    session = 'gazp'

    client = TelegramClient(session, api_id, api_hash, loop=loop)
    client.start()

    @client.on(events.NewMessage(chats=channel_source))
    async def handler(event):
        '''Забирает посты из телеграмм каналов и посылает их в наш канал'''

        if send_message_func is None:
            print(event.raw_text, '\n')
        else:
            await send_message_func(f'@prime1\n{event.raw_text}')

    return client


if __name__ == "__main__":

    client = telegram_parser()

    client.run_until_disconnected()
