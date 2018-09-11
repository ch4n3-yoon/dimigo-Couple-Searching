#!/usr/bin/env python2
# coding: utf-8

__author__ = 'ch4n3'

import requests
import json
import authkey

headers = {
    'Authorization': authkey.authkey
}
def getStayLists():
    r = requests.get('http://api.dimigo.life/service/stay', headers=headers)
    dump = json.loads(r.text)
    if dump['code'] != 200:
        return False
    return dump['data']

def getStay(stay_id):
    r = requests.get('http://api.dimigo.life/service/stay/apply/{0}'.format(stay_id), headers=headers)
    dump = json.loads(r.text)
    if dump['code'] != 200:
        return False
    return dump['data']

def getStayingDimigoin(stay_id):
    stay_info = getStay(stay_id)
    # print '[*] stay_id : {0}'.format(stay_id)
    stayDimigoins = []
    for i in range(len(stay_info)):
        user = {'user_id': stay_info[i]['user_id'], 'name': stay_info[i]['name'], 'seat': stay_info[i]['seat']}
        stayDimigoins.append(user)
    return stayDimigoins

def searchCouple(stay_id):
    dimigoins = getStayingDimigoin(stay_id)
    for dimi1 in dimigoins:
        seat1 = dimi1['seat']
        if seat1 == None:
            continue
        for dimi2 in dimigoins:
            seat2 = dimi2['seat']
            if seat2 == None:
                continue

            if seat1[0] == seat2[0]:
                num1 = int(seat1[1:])
                num2 = int(seat2[1:])
                if (num1 - 1) == num2 or (num1 + 1) == num2:
                    print "[*] 커플 발견"
                    print dimi1['name'],
                    print "♥",
                    print dimi2['name']




def main():
    stays = getStayLists()
    stayDimigoins = []
    for s in stays:
        stay_id = s['dates'][0]['stay_id']
        stay_info = getStay(stay_id)

        print '[*] stay_id : {0}'.format(stay_id)
        # for i in range(len(stay_info)):
        #     user = {'user_id': stay_info[i]['user_id'], 'name': stay_info[i]['name'], 'seat': stay_info[i]['seat']}
        #     stayDimigoins.append(user)

        print getStayingDimigoin(stay_id)
        searchCouple(stay_id)
    return stayDimigoins

if __name__ == '__main__':
    main()


