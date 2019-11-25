import read_file, write_file
import os

linkDatasets = './datasets/'
# fileName = 'giao_thong'
# fileLabelName = fileName + '.lb'
# listRawSents = read_file.read_line_to_sentenceList(linkDatasets, fileName + '.txt', '\n')
# numOfSent = len(listRawSents)
# listSentLabel = []
# strLabel = ''
# for sent in range(numOfSent//2):
#     # listSentLabel.append(underthesea.sentiment(sent)) # fasttext khong tuong thich windows
#     '''
#     chỗ này để gán nhãn cho dữ liệu không nhãn
#     if listRawSents[sent] is label a:
#         strLabel+='a, '
#     listSentLabel.append(last label)
#     '''
#     strLabel += '0, '
# for sent in range(numOfSent//2, numOfSent - 1):
#     strLabel += '1, '
# strLabel += '1'
# with open(linkDatasets + fileLabelName, 'w', encoding='utf-8') as f:
#     f.write(strLabel)
############################
## gộp file train.
# linkFolder = './SomeExample/1/'
linkFolder = './SomeExample/2/'
fileMergeName = 'giao_thong'
listDocName = os.listdir(linkFolder)
listAllDoc = []
listLabelStr = ''
negSent = []
posSent = []
neuSent = []
for fileName in listDocName:
    fileType = fileName[-6:]
    print(fileType)
    if fileType == '.clus0':
        negSent = read_file.read_line_to_sentenceList(linkFolder, fileName, '\n')
        for _ in range(len(negSent)):
            listLabelStr +='0, '
    elif fileType == '.clus1':
        posSent = read_file.read_line_to_sentenceList(linkFolder, fileName, '\n')
        for _ in range(len(posSent)):
            listLabelStr += '1, '
    elif fileType == '.clus2':
        neuSent = read_file.read_line_to_sentenceList(linkFolder, fileName, '\n')
        for _ in range(len(neuSent)):
            listLabelStr += '2, '
listAllDoc += negSent + posSent + neuSent
write_file.list_to_txt(listAllDoc, linkDatasets, fileMergeName + '.txt')
with open(linkDatasets + fileMergeName + '.lb', 'w', encoding='utf-8') as f:
    f.write(listLabelStr)