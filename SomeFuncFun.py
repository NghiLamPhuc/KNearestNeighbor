from Point import Point
import read_file
import write_file
import os
import underthesea

def main():
    ### chuyen train_vn tu co label sang không label. train_vn do.an2
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
    
    
    
if __name__=="__main__": main()