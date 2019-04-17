
import requests

from urllib.parse import urlencode


def generates_link_with_token():
    """  Формирует ссылку, для получения токена если токен устарел, копируем токент после 'access_token=' до знака '&'
    и вставляем в значение 'TOKEN =' ниже под функцией
    """
    AUTH_URL = 'https://oauth.vk.com/authorize'
    APP_ID = 6927892
    AUTH_DATA = {
        'client_id': APP_ID,
        'display': 'page',
        # redirect_uri='https://oauth.vk.com/blank.html';
        'scope': 'friends',
        'response_type': 'token',
        'v': 5.74
    }

    print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))


TOKEN = 'f49c264bb2cb15374666bc40d51efc240d589fd806c33107e3fcc84045073c3755b70875200146e36c33c'


def finding_mutual_friends(source_id, target_id):
    """  Находит общих друзей между двумя пользователями, на ввод принимает id двух пользователей,
    выводит ссылки на общих друзей"""
    response = requests.get(
        'https://api.vk.com/method/friends.getMutual',
        params=dict(
            access_token=TOKEN,
            v='5.52',
            source_uid=source_id,
            target_uid=target_id

        )
    )
    for id in (response.json()['response']):
        print('https://vk.com/id' + str(id))


source_id = input('введите id  первого пользователя')
target_id = input('введите id второго пользователя')
finding_mutual_friends(source_id, target_id)



