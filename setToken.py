#!/usr/bin/python
# coding: utf-8

import requests
import json

id_ = 'id'
pwd = 'password'

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

