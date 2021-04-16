import requests
import os


def get_anti_ad():
    res = requests.get('https://anti-ad.net/domains.txt')
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text


if __name__ == '__main__':
    ad = get_anti_ad()
    ad = ad.split('\n')
    ad_file = open(os.getcwd() + '/temp/ad.txt', mode='w', encoding='utf-8')
    ad_snip = open(os.getcwd() + '/snippet/ad.txt', mode='w', encoding='utf-8')
    for line in ad:
        if not line.startswith('#') and len(line) > 0:
            ad_file.write('DOMAIN-SUFFIX,%s,REJECT\n' % line)
            ad_snip.write('DOMAIN-SUFFIX,%s\n' % line)
    ad_file.close()
    ad_snip.close()
