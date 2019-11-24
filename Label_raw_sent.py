import read_file, write_file

linkDatasets = './datasets/'
fileName = 'giao_thong'
fileLabelName = fileName + '.lb'
listRawSents = read_file.read_line_to_sentenceList(linkDatasets, fileName + '.txt', '\n')
numOfSent = len(listRawSents)
listSentLabel = []
strLabel = ''
for sent in range(numOfSent//2):
    # listSentLabel.append(underthesea.sentiment(sent)) # fasttext khong tuong thich windows
    '''
    chỗ này để gán nhãn cho dữ liệu không nhãn
    if listRawSents[sent] is label a:
        strLabel+='a, '
    listSentLabel.append(last label)
    '''
    strLabel += '0, '
for sent in range(numOfSent//2, numOfSent - 1):
    strLabel += '1, '
strLabel += '1'
with open(linkDatasets + fileLabelName, 'w', encoding='utf-8') as f:
    f.write(strLabel)
