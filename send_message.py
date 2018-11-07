import translate,time,requests



def request_get(token,user_id,text,ts ,server,key):
    req = requests.get('https://api.vk.com/method/messages.send',
                 params={'access_token': token,
                         'user_id': user_id,
                         'group_id': 171555042,
                         'message': text,
                         'v': 5.87})
    request = requests.get(server,
                           params={'act': 'a_check', 'key': key, 'ts': ts, 'wait': 40}).json()
    ts = request['ts']
    return ts


def set_time(token,user_id):
    request_set_time = request_message = requests.get('https://api.vk.com/method/messages.send',
                                       params={'access_token':token,
                                               'user_id':user_id,
                                               'group_id':171555042,
                                               'message':'Установите время',
                                               'v':5.87})


def morning_message(token):
    import random
    text = ['Доброе утро. Надеюсь сегодня ты споткнёшься и упадёшь в лужу',
            'Добрейшее утречко. Для хорошего начала дня, облейся кофе',
            'Доброе. Ты до сих пор жив? Странно.',
            'Привет. Чо каво?',
            'Доброе утро! Сегодня отличный день, чтобы никуда не ехать!!!',
            'Кто-то щас спит, а тебе идти на уёбу. Ну или работу. Всё равно страдай',
            'Жизнь - это унижение, страдание, БОЛЬ'
            ]

    file = open('Users','r')
    weather = translate.translate_weather()
    print('from weather')
    print(weather)
    message = 'ПРОГНОЗ ПОГОДЫ НА СЕГОДНЯ:\n''Сегодня ожидается: '\
              +weather[0]+','+weather[1]+'\n'+'Температура будет примерно:'\
              +str(weather[2])+u'\u2103 \n'+'Оденьтесь потеплее <3'

    for i in(file):
        # print(i.strip())
        # image = gay_image.image
        request_message = requests.get('https://api.vk.com/method/messages.send',
                                       params={'access_token':token,
                                               'user_id':i.strip(),
                                               'group_id':171555042,
                                               'message':text[random.randint(0, len(text)-1)]+'\n'+
                                                         message,
                                               'v':5.87})
        print(request_message.json())
    time.sleep(3700)
    # time.sleep()
    # new_server()


def weather_now(token,user_id):
    weather_now = translate.translate_weather_now()
    request_message = requests.get('https://api.vk.com/method/messages.send',
                                       params={'access_token':token,
                                               'user_id':user_id,
                                               'group_id':171555042,
                                               'message':str(weather_now[0])+u'\u2103 \n',
                                               'v':5.87})

def game(token,user_id,server,ts,key):
    import random

    text = 'Сейчас ты буешь участвовать в дуэли. ' \
           'Посмотрим, кто самый быстрый \n' \
           'Надеюсь ты готов. \n' \
           'Тебе нужно будет решить пример быстрее, чем истечёт время!!!\n' \
           'Приготовься. Пример появится через 10 секунд.'
    request_get(token, user_id, text, ts, server,key)
    time.sleep(7)

    for i in range(3):
        text = 3-i
        request_get(token,user_id,text,ts,server,key)
        time.sleep(1)

    a = random.randint(0,10)
    b = random.randint(0,10)
    task = a*b

    text = str(a)+'*'+str(b)
    ts = request_get(token,user_id,text,ts,server,key)

    clock = random.randint(3,5)
    request = requests.get(server,
                           params={'act': 'a_check',
                                   'key': key, 'ts': ts,
                                   'wait': clock}).json()  # New event

    text = 'Пиф-паф. Улица затихла после высрелов.\n' \
           '"Перекати поле"\n' \
           'И... Один из дуэлянтов падает на колени.\n' \
           'У вас темнеет в глазах и...'
    request_get(token, user_id, text,ts,server,key)
    try:
        if request['updates'][0]['type']=='message_new' and \
                    request['updates'][0]['object']['text'] == str(task):
            text = 'А ты везучий...\n' \
               'Видимо у тебя самая быстрая лапка на диком западе'
        else:
            text = 'Ты мёртв.\n' \
                   'Теперь ты сюда не можешь писать час'
    except IndexError:
        text = 'Ты мёртв.\n' \
               'Теперь ты сюда не можешь писать час'




    request_get(token, user_id, text,ts,server,key)

