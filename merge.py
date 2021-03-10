import os


def get_index(lines):
    index = 0
    for line in lines:
        index += 1
        if line == '[Rule]\n':
            return index


if __name__ == '__main__':
    parent_path = os.getcwd()
    print(parent_path)
    file_1 = open(parent_path + '/Complete.conf', mode='r')
    file_2 = open(parent_path + '/UnblockNeteaseMusic.conf', mode='r')
    file_merge = open(parent_path + '/merge.conf', mode='w')
    lines_1 = file_1.readlines()
    lines_2 = file_2.readlines()
    index1 = get_index(lines_1)
    index2 = get_index(lines_2)

    for i in range(0, index1):
        file_merge.write(lines_1[i])

    for i in range(index2, len(lines_2) - 2):
        file_merge.write(lines_2[i])

    flag_1 = False
    for i in range(index1, len(lines_1)):
        if (lines_1[i] == '# > Netease Music\n'):
            flag_1 = True

        if (flag_1 and len(lines_1[i]) <= 1):
            flag_1 = False

        if (not flag_1):
            file_merge.write(lines_1[i])

    file_1.close()
    file_2.close()
    file_merge.close()
