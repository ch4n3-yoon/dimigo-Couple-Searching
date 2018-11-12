#!/usr/bin/python
# coding: utf-8

import requests
import json

<<<<<<< HEAD
id_ = 'ch4n3-yoon'
pwd = 'rudska306'
=======
id_ = '*********'
pwd = '*********'
>>>>>>> d4ea6f8b19b07381500141dcdf93e8e96c58e6fe

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def set_token():
    data = {
        'id': id_,
        'pwd': pwd,
    }

    r = requests.post("http://api.dimigo.life/users/login",
                          data=data, headers=headers)
    loginData = json.loads(r.text)
    return loginData['token']

