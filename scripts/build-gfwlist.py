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
    ad = get_gfw()
    ad = ad.split('\n')
    ad_file = open(os.getcwd() + '/temp/gfw.txt', mode='w', encoding='utf-8')
    for line in ad:
        if not line.startswith('#'):
            ad_file.write('%s,Proxy\n' % line)
    ad_file.close()
