from collections import defaultdict
from Point import Point

# Hàm đọc file dạng nhiều dòng, mỗi dòng là transaction.
# mỗi transaction chứa item.
def read_input_file_to_dict(link, fileName, splitType) -> dict:
    f = open(link + fileName, 'r', encoding = 'utf-8')
    inpDict = defaultdict(dict)
    i = 0
    for line in f:
        inpDict[i] = sorted(line.rstrip().split(splitType))
        i += 1
    f.close()
    return inpDict
# Hàm đọc file dạng nhiều dòng, mỗi dòng là transaction.
# Cột đầu tiên là tên transaction.
def read_input_file_with_row_name_to_dict(link, fileName, splitType) -> dict:
    f = open(link + fileName, 'r', encoding = 'utf-8')
    inpDict = defaultdict(dict)
    for line in f:
        lineToList = line.rstrip().split(splitType)
        rowName = lineToList[0]
        items = lineToList[1:]
        inpDict[rowName] = sorted(items)
    f.close()
    return inpDict

def str_to_dict(file: str, splitType) -> dict:
    inpDict = defaultdict(dict)
    strToList = file.rstrip().split('\n')
    for line in strToList:
        lineToList = line.rstrip().split(splitType)
        rowName = lineToList[0]
        items = lineToList[1:]
        inpDict[rowName] = sorted(items)
    return inpDict

def read_lines_to_list(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    List = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)
            List.append(lineToAdd)
    f.close()
    return List

def read_lines_to_floatlist(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    List = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)#[1:-1]
            lineToAdd[0] = lineToAdd[0][1:]
            lineToAdd[-1] = lineToAdd[-1][:-1]
            lineToFloat = [float(numStr) for numStr in lineToAdd]
            List.append(lineToFloat)
    f.close()
    return List

def read_lines_to_intlist(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    List = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)
            ## [1, 2, 3] neu co [ ] thi moi dung 2 dong nay
            # lineToAdd[0] = lineToAdd[0][1:]
            # lineToAdd[-1] = lineToAdd[-1][:-1]
            lineToInt = [int(numStr) for numStr in lineToAdd]
            List.append(lineToInt)
    f.close()
    if len(List) == 1:
        return list(sum(List, []))
    return List

def read_lines_to_listPoint(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    List = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)#[1:-1]
            lineToAdd[0] = lineToAdd[0][1:]
            lineToAdd[-1] = lineToAdd[-1][:-1]
            lineToFloat = [float(numStr) for numStr in lineToAdd]
            List.append(lineToFloat)
    f.close()
    listPoints = []
    for vec in List:
        listPoints.append(Point(vec))
    return listPoints


def read_lines_to_floatlist_nonSquareBracklets(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    List = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)#[1:-1]
            # bỏ 2 cái ngoặc vuông
            # lineToAdd[0] = lineToAdd[0][1:]
            # lineToAdd[-1] = lineToAdd[-1][:-1]
            lineToFloat = [float(numStr) for numStr in lineToAdd]
            List.append(lineToFloat)
    f.close()
    return List


def read_input_file_to_int(link, fileName) -> int:
    num = 0
    f = open(link + fileName, 'r', encoding = 'utf-8')
    num = int(f.read())
    f.close()
    return num

def read_line_to_sentenceList(link, fileName, splitType) -> list:
    f = open(link + '/' + fileName, 'r', encoding = 'utf-8')
    sentences = list()
    for line in f:
        if line != '\n':
            lineToAdd = line.rstrip().split(splitType)
            sentences.append(''.join(lineToAdd))
    f.close()
    return sentences