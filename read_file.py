'lamphucnghi@gmail.com'
from collections import defaultdict

TYPE_OF_RESULT_LIST_IS_TEXT = 0
TYPE_OF_RESULT_LIST_IS_INT = 1
TYPE_OF_RESULT_LIST_IS_FLOAT = 2
TYPE_OF_RESULT_LIST_IS_SENTENCE = 3

'''
hàm này chưa cần. Sửa sau.
'''
def read_line_to_dict(folderName: str, fileName: str, fileType: str, splitType: str) -> dict:
    f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
    inpDict = defaultdict(dict)
    i = 0
    for line in f:
        inpDict[i] = sorted(line.rstrip().split(splitType))
        i += 1
    f.close()
    return inpDict

'''
reading a file as:
key abc a b das wf sds ...
line[0] play as key.
value is a list.
'''
def read_line_to_dict_key_first_value_list(folderName: str, fileName: str, fileType: str, splitType: str) -> dict:
    f = open('./{0}/{1}{2}'.format(folderName, fileName, fileType), 'r', encoding = 'utf-8')
    inpDict = defaultdict(dict)
    for line in f:
        lineToList = line.rstrip().split(splitType)
        rowName = lineToList[0]
        items = lineToList[1:]
        inpDict[rowName] = sorted(items)
    f.close()
    return inpDict

'''
Reading a file like:
[0.1 0.2 0.3....]

'''
def read_lineSplited_to_list(folderName: str, fileName: str, fileType: str, splitType: str, outListType: int) -> list:
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
    return List
'''
We have a [L]ist with each item is a [l]ist.
We want to merge all item of all [l]ist to [L]ist.
[[0, 1, 2], [1, 2, 3]] --> [0, 1, 2, 1, 2, 3]
'''
def convert_twoHierachyList_to_oneList(inpList: list(list())) -> list:
    return list(sum(inpList, []))

def main():
    print('readfile')
    # folderName = 'datasets'
    # fileName = 'giao_thong'
    # fileType = '.txt'
    # a = read_lineSplited_to_list(folderName, fileName, fileType, ' ', 3)
    # print(a[0])

if __name__ == "__main__": main()