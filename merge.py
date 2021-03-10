import os


def get_index(file):
    index = 0
    lines = file.readlines()
    for line in lines:
        index += 1
        if line == '[Rule]\n':
            return index, lines


if __name__ == '__main__':
    parent_path = os.getcwd()
    file_1 = open(parent_path + '/Complete.conf', mode='r')
    file_2 = open(parent_path + '/UnblockNeteaseMusic.conf', mode='r')
    file_merge = open(parent_path + '/merge.conf', mode='w')
    index1, lines_1 = get_index(file_1)
    index2, lines_2 = get_index(file_2)

    for i in range(0, index1):
        file_merge.write(lines_1[i])

    for i in range(index2, len(lines_2) - 2):
        file_merge.write(lines_2[i])

    for i in range(index1, len(lines_1)):
        file_merge.write(lines_1[i])

    file_1.close()
    file_2.close()
    file_merge.close()
