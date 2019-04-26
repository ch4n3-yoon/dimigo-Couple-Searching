#!/usr/bin/env python2
# coding: utf-8

import requests
import json
import setToken

__author__ = 'ch4n3'

stayingDimigoins = {}
couples = []

authkey = setToken.set_token()
headers = {
    'Authorization': authkey
}

def chk200(code):
    if code != 200:
        return True
    else:
        return False


def getStayLists():
    r = requests.get('http://api.dimigo.life/service/stay', headers=headers)
    dump = json.loads(r.text)
    if dump['code'] != 200:
        return False
    return dump['data']


def getAllStayIds():
    stay_ids = []
    stays = getStayLists()
    for s in stays:
        stay_ids.append(s['dates'][0]['stay_id'])
    return stay_ids


allStayIds = getAllStayIds()


def getStay(stay_id):
    r = requests.get(
        'http://api.dimigo.life/service/stay/apply/{0}'.format(stay_id),
        headers=headers)

    try:
        dump = json.loads(r.text)
    except ValueError:
        print "[*] json parsing failed"
        return False
    if dump['code'] != 200:
        return False
    return dump['data']


def getStayingDimigoin(stay_id):
    stay_info = getStay(stay_id)
    if stay_info is False:
        return False

    stayDimigoins = []
    for i in range(len(stay_info)):
        user = {'user_id': stay_info[i]['user_id'],
                'name': stay_info[i]['name'],
                'seat': stay_info[i]['seat'],
                'gender': stay_info[i]['gender']}
        stayDimigoins.append(user)

    return stayDimigoins


def searchCouple(stay_id):
    if stay_id in stayingDimigoins.keys():
        dimigoins = stayingDimigoins[stay_id]
    else:
        stayingDimigoins[stay_id] = getStayingDimigoin(stay_id)
        dimigoins = stayingDimigoins[stay_id]

    if dimigoins is False:
        return False

    # print dimigoins
    for dimi1 in dimigoins:
        seat1 = dimi1['seat']
        if seat1 is None:
            continue
        for dimi2 in dimigoins:
            seat2 = dimi2['seat']
            if seat2 is None:
                continue
            if dimi1['gender'] == dimi2['gender']:
                continue
            if len(seat1) == 0 or len(seat2) == 0:
                continue

            if seat1[0] == seat2[0]:
                try:
                    num1 = int(seat1[1:])
                    num2 = int(seat2[1:])
                except TypeError:
                    continue
                if abs(num1 - num2) == 1:

                    # try:
                    #    lib.t.start()
                    # except RuntimeError:
                    #     pass
                    if checkCouple(stay_id,
                                   dimi1['user_id'],
                                   dimi2['user_id']):
                        if not isAlreadySearched(dimi1, dimi2):
                            # print "[*] 커플 발견"
                            # print dimi1['name'],
                            # print "♥",
                            # print dimi2['name']

                            couples.append({dimi1['gender']: dimi1['name'],
                                            dimi2['gender']: dimi2['name']})
                    # done = True


def isCouple(stay_id, user_id1, user_id2):
    if stay_id in stayingDimigoins.keys():
        dimigoins = stayingDimigoins[stay_id]
    else:
        stayingDimigoins[stay_id] = getStayingDimigoin(stay_id)
        dimigoins = stayingDimigoins[stay_id]

    for dimi1 in dimigoins:
        if dimi1['user_id'] != user_id1:
            continue
        for dimi2 in dimigoins:
            if dimi2['user_id'] != user_id2:
                continue

            # 잔류 좌석 미선택자를 위한 예외 처리
            if dimi1['seat'] is None or dimi2['seat'] is None:
                continue

            try:
                if dimi1['seat'][0] == dimi2['seat'][0]:
                    seat1 = int(dimi1['seat'][1:])
                    seat2 = int(dimi2['seat'][1:])

                    if abs(seat2 - seat1) == 1:
                        return True
            except IndexError:
                return False
    return False


def checkCouple(searchedStayId, user_id1, user_id2):
    stay_ids = allStayIds
    index = stay_ids.index(searchedStayId)

    search_ids = []
    if (index - 2) < 0:
        for i in range(0, index + 3):
            search_ids.append(stay_ids[i])
    else:
        for i in range(index - 2, index + 3):
            try:
                search_ids.append(stay_ids[i])
            except IndexError:
                pass
    search_ids.remove(searchedStayId)
    stay_ids = search_ids
    # print "[*] Searching ...",
    # print stay_ids

    cnt = 1
    for stay_id in stay_ids:
        result = isCouple(stay_id, user_id1, user_id2)
        if result:
            cnt += 1
        if cnt >= 3:
            return True
    return False


def isAlreadySearched(user1, user2):
    for c in couples:
        if c[user1['gender']] == user1['name'] \
                and c[user2['gender']] == user2['name']:
            return True
    return False


def printCouples():
    for c in couples:
        print c['M'],
        print '♥',
        print c['F']


def main():
    stays = getStayLists()
    for s in stays:
        stay_id = s['dates'][0]['stay_id']

        print '[*] stay_id : {0}'.format(stay_id),
        print '({0})'.format(s['dates'][0]['stay_date'])

        searchCouple(stay_id)
    printCouples()


if __name__ == '__main__':
    main()
