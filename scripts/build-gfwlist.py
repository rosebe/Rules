import requests
import os
import re
import base64


def get_gfw():
    res = requests.get(
        'https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/gfw.txt')
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text


if __name__ == '__main__':
    gfw = get_gfw()
    gfw = gfw.split('\n')
    gfw_file = open(os.getcwd() + '/temp/gfw.txt', mode='w', encoding='utf-8')
    for line in gfw:
        if len(line) > 0:
            gfw_file.write('%s,Proxy\n' % line)
    gfw_file.close()
