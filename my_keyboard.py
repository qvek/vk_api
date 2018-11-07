import requests,json


def main_keyboard(token,user_id):
    print('keyboard')
    keyboard_param={'one_time':False,
                    'buttons':[
                        [{'action':
                                {'type':'text',
                                 'label':'set time'},
                          'color':'negative'}],
                    [{'action':
                          {'type':'text',
                           'label':'wanna know weather'},
                             'color':'primary'}],
                    [{'action':
                          {'type':'text',
                           'label':'Wanna play game'},
                    'color':'positive'}]
                    ]}
    requests.get('https://api.vk.com/method/messages.send',
                params={'user_id':user_id,
                        'access_token':token,
                        'v':5.87,
                        'message':'что хотите?',
                        'keyboard':json.dumps(keyboard_param)
                                   })
    return

def set_time(token,user_id):
    keyboard_params = {'one_time':False,
                    'buttons':[
                        [{'action':
                                {'type':'text',
                                 'label':'8:00'
                                 },
                             'color':'negative'
                             },
                         {'action':
                              {'type': 'text',
                               'label': '9:00'
                               },
                          'color': 'negative'
                          },
                         {'action':
                              {'type': 'text',
                               'label': '10:00'
                               },
                          'color': 'negative'
                          }
                        ]]}
    key = requests.get('https://api.vk.com/method/messages.send',
                       params={'user_id': user_id,
                               'access_token': token,
                               'v': 5.87,
                               'message': 'что хотите?',
                               'keyboard': json.dumps(keyboard_params)
                               })






