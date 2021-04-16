import os
import time
import re


def get_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content


values = {
    'build_time': time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    'gfw': get_from_file(os.getcwd() + '/temp/gfw.txt'),
    'netease': get_from_file(os.getcwd() + '/temp/netease.txt'),
    'ad': get_from_file(os.getcwd() + '/temp/ad.txt'),
    'telegram': get_from_file(os.getcwd() + '/temp/telegram.txt')
}

if __name__ == '__main__':
    template_file = open(os.getcwd() + '/template/merge-gfw-template.conf', mode='r', encoding='utf-8')
    template = template_file.read()
    output_file = open(os.getcwd() + '/gfw-ad-netease.conf', mode='w', encoding='utf-8')
    marks = re.findall(r'{{(.+)}}', template)
    for mark in marks:
        template = template.replace('{{' + mark + '}}', values[mark])
    output_file.write(template)
    template_file.close()
    output_file.close()
