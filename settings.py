HERON_DOMAIN = 'http://127.0.0.1:8000/bots'

from local_settings import *

BOT_ONLINE_ENDPOINT = '/'.join([HERON_DOMAIN, 'discord', 'bot_online'])
MESSAGE_QUERY_ENDPOINT = '/'.join([HERON_DOMAIN, 'discord', 'get_message'])
