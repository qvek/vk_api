import requests,datetime,my_keyboard, send_message

def new_server():
    token = '23164a921a9695b031d3be4a283fc874fe0c073e973d3e8ce0b7ad9d2b7716b3ba9ed3ddebc3061edd883'
    data = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                        params={'access_token': token, 'v': 5.87,
                                'group_id': 171555042}).json()  # получение ответа от сервера
    key = data['response']['key']
    server = data['response']['server']
    ts = data['response']['ts']
    query(key,server,ts,token)


def query(key,server,ts,token):   #send query
    while True:
        request = requests.get(server,
                       params={'act':'a_check','key':key,'ts':ts,'wait':40}).json() #New event
        print(request)


        try:
            ts = request['ts']
        except KeyError:
            new_server()


        if request['updates']==[]:
            pass
        elif request['updates'][0]['type']=='message_allow':
            ids = str(request['updates'][0]['object']['from_id'])
            new_user(ids)
        elif request['updates'][0]['type']=='message_new':
            user_id = request['updates'][0]['object']['from_id']
            if request['updates'][0]['object']['text'] == 'set time':
                my_keyboard.set_time(token,user_id)
            elif request['updates'][0]['object']['text'] == 'wanna know weather':
                send_message.weather_now(token,user_id)
            elif request['updates'][0]['object']['text'] == 'Wanna play game':
                send_message.game(token,user_id,server,ts,key)





            else:
                user_id = request['updates'][0]['object']['from_id']
                my_keyboard.main_keyboard(token, user_id)


        else:
            pass



        time_now = datetime.datetime.now()

def new_user(ids):  #Add new user in file
    file = open('Users','r+')
    for i in(file):
        if str(ids)==str(i.strip()):
            file.close()
            return
    file.write(str(ids)+'\n')
    file.close()
    return


new_server()