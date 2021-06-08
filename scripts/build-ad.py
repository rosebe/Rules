import requests
import os


def get_ad(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')

anti_ad_url = 'https://anti-ad.net/surge.txt'
reject_url = 'https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/reject.txt'

if __name__ == '__main__':
    anti_ad = get_ad(anti_ad_url)
    reject = get_ad(reject_url)
    anti_ad = set(anti_ad)
    reject = set(reject)
    ad = reject.union(anti_ad)
    ad = list(ad)
    ad.sort()
    ad_file = open(os.getcwd() + '/temp/ad.txt', mode='w', encoding='utf-8')
    for line in ad:
        if not line.startswith('#') and len(line) > 0:
            ad_file.write('%s,REJECT\n' % line)
    ad_file.close()
