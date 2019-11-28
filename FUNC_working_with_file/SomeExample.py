from Point import Point
import read_file
import write_file
import os
import underthesea

def main():
    ### chuyen train_vn tu co label sang không label.
    # a = read_lines_to_list('./datasets/', 'train_vn.txt', ' ')
    # for ia in a:
    #     del ia[-1]
    #     for num in range(len(ia)):
    #         ia[num] = float(ia[num])
    # write_file.list_to_txt(a, './datasets/', 'train_vn_nonLabel.vector')
    # b = read_file.read_lines_to_floatlist('./datasets/', 'train_vn_nonLabel.vector', ', ')
    # c = read_file.read_lines_to_floatlist_nonSquareBracklets('./datasets/', 'train_vn_nonLabel.vector', ', ')
    ### gộp file
    # linkFolder = './datasets/giao-thong/'
    # listDocName = os.listdir(linkFolder)
    # listAllDoc = []
    # for fileName in listDocName:
    #     listAllDoc.append(read_file.read_line_to_sentenceList(linkFolder, fileName, '\n')[1:])
    # listDocToSent = []
    # for doc in listAllDoc:
    #     for clusText in doc:
    #         listDocToSent += underthesea.sent_tokenize(clusText)
    # write_file.list_to_txt(listDocToSent, './datasets/', 'giao_thong.txt')
    ### tach giao_thong theo cluster
    fileName = 'giao_thong.txt'
    nameclus0 = 'giaothongclus0.clus'
    nameclus1 = 'giaothongclus1.clus'
    nameclus2 = 'giaothongclus2.clus'
    clus0 = read_file.read_lines_to_intlist_nonSquareBracklets('./SomeExample', nameclus0, ' ')[0]
    clus1 = read_file.read_lines_to_intlist_nonSquareBracklets('./SomeExample', nameclus1, ' ')[0]
    clus2 = read_file.read_lines_to_intlist_nonSquareBracklets('./SomeExample', nameclus2, ' ')[0]
    listRawText = read_file.read_line_to_sentenceList('./SomeExample/', fileName, '\n')
    listRawClus0 = []
    listRawClus1 = []
    listRawClus2 = []
    for iSent in range(len(listRawText)):
        if iSent in clus0:
            listRawClus0.append(listRawText[iSent])
        elif iSent in clus1:
            listRawClus1.append(listRawText[iSent])
        elif iSent in clus2:
            listRawClus2.append(listRawText[iSent])
    write_file.list_to_txt(listRawClus0, 'SomeExample', 'giao_thong_clus0.txt')
    write_file.list_to_txt(listRawClus1, 'SomeExample', 'giao_thong_clus1.txt')
    write_file.list_to_txt(listRawClus2, 'SomeExample', 'giao_thong_clus2.txt')

if __name__=="__main__": main()