'lamphucnghi@gmail.com'
from collections import defaultdict

TYPE_OF_RESULT_LIST_IS_TEXT = 0
TYPE_OF_RESULT_LIST_IS_INT = 1
TYPE_OF_RESULT_LIST_IS_FLOAT = 2
TYPE_OF_RESULT_LIST_IS_SENTENCE = 3

TYPE_OF_CONVERT_STR = 10
TYPE_OF_CONVERT_INT = 11
TYPE_OF_CONVERT_FLOAT = 12

'''
read to dict
key is index of row
value is row
'''
def read_line_to_dict(folderName: str, fileName: str, fileType: str, splitType: str) -> dict:
    try:
        f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
        inpDict = defaultdict(dict)
        i = 0
        for line in f:
            if line != '\n':
                inpDict[i] = sorted(line.rstrip().split(splitType))
                i += 1
        f.close()
        return inpDict
    except:
        print('No such file or dir!!')
'''
reading a file with dict type:
key1 : value1, value2, value3, ...
key2 : value1, value2, ....
'''
def read_dictLine(folderName: str, fileName: str, fileType: str, splitType: str, keyType: int, valueType: int) -> dict:
    try:
        f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
        inpDict = defaultdict(dict)
        for line in f:
            if line != '\n':
                lineSplited = line.split(' : ')
                rKey = lineSplited[0]
                rValue = lineSplited[1]
                rValueSplited = rValue.rstrip().split(splitType)

                if keyType == TYPE_OF_CONVERT_STR:
                    rKey = lineSplited[0]
                elif keyType == TYPE_OF_CONVERT_INT:
                    rKey = int(lineSplited[0])
                elif keyType == TYPE_OF_CONVERT_FLOAT:
                    rKey = float(lineSplited[0])

                if valueType == TYPE_OF_CONVERT_STR:
                    rValue = lineSplited[1]
                    inpDict[rKey] = sorted(rValueSplited)
                elif valueType == TYPE_OF_CONVERT_INT:
                    rValueChanged = [int(value) for value in rValueSplited]
                    inpDict[rKey] = sorted(rValueChanged)
                elif valueType == TYPE_OF_CONVERT_FLOAT:
                    rValueChanged = [float(value) for value in rValueSplited]
                    inpDict[rKey] = sorted(rValueChanged)
        f.close()
        return inpDict
    except:
        print('No such file or dir!!')
'''
reading a file as:
key abc a b das wf sds ...
line[0] play as key.
value is a list.
'''
def read_line_to_dict_key_first_value_list(folderName: str, fileName: str, fileType: str, splitType: str) -> dict:
    try:
        f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
        inpDict = defaultdict(dict)
        for line in f:
            lineToList = line.rstrip().split(splitType)
            rowName = lineToList[0]
            items = lineToList[1:]
            inpDict[rowName] = sorted(items)
        f.close()
        return inpDict
    except:
        print('No such file or dir!!')

'''
Reading a file like:
[*0.1 0.2 0.3....
0.4 0.5 0.6]*
each row stored in a [l]ist of [L]ist
'''
def read_lineSplited_to_list(folderName: str, fileName: str, fileType: str, splitType: str, outListType: int) -> list:
    try:
        f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
        List = list()
        for line in f:
            if line != '\n':
                if outListType == TYPE_OF_RESULT_LIST_IS_SENTENCE:
                    List.append(line.rstrip())
                else:
                    lineToStrList = line.rstrip().split(splitType)
                    if lineToStrList[0][0] == '[':
                        lineToStrList[0] = lineToStrList[0][1:]
                        lineToStrList[-1] = lineToStrList[-1][:-1]
                    if outListType == TYPE_OF_RESULT_LIST_IS_TEXT:
                        List.append(lineToStrList)
                    elif outListType == TYPE_OF_RESULT_LIST_IS_INT:
                        List.append([int(x) for x in lineToStrList])
                    elif outListType == TYPE_OF_RESULT_LIST_IS_FLOAT:
                        List.append([float(x) for x in lineToStrList])
                
        f.close()
        if len(List) == 1:
            return sum(List, [])
        return List
    except:
        print('No such file or dir!!')
'''
We have a [L]ist with each item is a [l]ist.
We want to merge all item of all [l]ist to [L]ist.
[[0, 1, 2], [1, 2, 3]] --> [0, 1, 2, 1, 2, 3]
'''
def convert_twoHierachyList_to_oneList(inpList: list(list())) -> list:
    return list(sum(inpList, []))

def test():
    folderName = 'test_write'
    fileName = ['a1', 'an', 'b', 'c', 'd', 'e']
    fileType = '.txt'
    a1 = read_lineSplited_to_list(folderName, fileName[0], fileType, ', ', 1)
    print(a1)
    an = read_lineSplited_to_list(folderName, fileName[1], fileType, ', ', 1)
    print(an)
    b1 = read_line_to_dict(folderName, fileName[2], fileType, ', ')
    print(b1)
    bn = read_line_to_dict(folderName, fileName[1], fileType, ', ')
    print(bn)
    c1 = read_line_to_dict(folderName, fileName[3], fileType, ', ')
    print(c1)
    c2 = read_dictLine(folderName, fileName[3], fileType, ', ', TYPE_OF_CONVERT_STR, TYPE_OF_CONVERT_FLOAT)
    print(c2)
    d1 = read_line_to_dict(folderName, fileName[4], fileType, ', ')
    print(d1)
    d2 = read_dictLine(folderName, fileName[4], fileType, ', ', TYPE_OF_CONVERT_STR, TYPE_OF_CONVERT_FLOAT)
    print(d2)

    e = read_dictLine(folderName, fileName[4], fileType, ', ', TYPE_OF_CONVERT_STR, TYPE_OF_CONVERT_STR)
    print(e)


def main():
    print('readfile')
    

if __name__ == "__main__": main()