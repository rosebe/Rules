import requests
import os
import re
import base64


# Refer to the code of h2y: https://github.com/h2y/Shadowrocket-ADBlock-Rules/blob/master/factory/gfwlist.py

def get_gfw():
    res = requests.get('https://cdn.jsdelivr.net/gh/Loukky/gfwlist-by-loukky/gfwlist.txt')
    if res.status_code != 200:
        raise Exception('Connect error')
    return base64.b64decode(res.text).decode('utf-8').replace('\\n', '\n')


if __name__ == '__main__':
    gfw = get_gfw()
    gfw = gfw.split('\n')
    domain_list = []
    rules_formated = []
    gfw_file = open(os.getcwd() + '/temp/gfw.txt', mode='w', encoding='utf-8')

    for row in gfw:
        row = row.strip()

        # 注释 直接跳过
        if row == '' or row.startswith('!') or row.startswith('@@') or row.startswith('[AutoProxy'):
            continue

        # 清除前缀
        row = re.sub(r'^\|?https?://', '', row)
        row = re.sub(r'^\|\|', '', row)
        row = row.lstrip('.*')

        # 清除后缀
        row = row.rstrip('/^*')

        rules_formated.append(row)

    rules_filtered = []
    for rule in rules_formated:
        if '/' in rule:
            split_rule = rule.split('/')
            rule = split_rule[0]
        if not re.match('^[\w.-]+$', rule):
            continue
        rules_filtered.append(rule)
        rules_filtered = list(set(rules_filtered))
        rules_filtered.sort()
    for rule in rules_filtered:
        gfw_file.write('DOMAIN-SUFFIX,%s,Proxy\n' % rule)

    # for line in gfw:
    #     if re.findall('^\!|\[|^@@|^\d+\.\d+\.\d+\.\d+', line):
    #         continue
    #     else:
    #         domain = re.findall('([\w\-\_]+\.[\w\.\-\_]+)[\/\*]*', line)
    #         if domain:
    #             try:
    #                 found = domain_list.index(domain[0])
    #             except ValueError:
    #                 if "spotify.com" in domain[0]:
    #                     continue
    #                 else:
    #                     domain_list.append(domain[0])
    #                     gfw_file.write('DOMAIN-SUFFIX,%s,Proxy\n' % (domain[0]))
    #         else:
    #             continue
    gfw_file.close()
