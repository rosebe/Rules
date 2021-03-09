import os

if __name__ == '__main__':
    parent_path = os.getcwd()
    file = open(parent_path + '/Complete.conf', mode='r', encoding='UTF-8')
    index1 = 0
    for line in file.readlines():
        index1 += 1
        if line == '[Rule]\n':
            break
    file = open(parent_path + '/merge.conf', mode='w', encoding='UTF-8')
    file.write('file1')
    print(index1)
