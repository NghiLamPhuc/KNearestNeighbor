from Point import Point
import read_file, write_file, make_folder
import underthesea
import fasttext

DATASETS_IS_VECTOR = 1
DATASETS_IS_TEXT = 0

class KNearestNeighbor:
    '''
    dataInitType:  Kiểu dữ liệu là 0 vector hay 1 text.
                   datasets is vectorized or raw sentence.
    dataInit: list dataset
    dType: distance type: 0 eulcidean
    dataName: tên file dữ liệu train.
              datasets name.
    '''
    def __init__(self, dataInitType: int, dataInit: list, k: int, label: list, dType: int, dataName: str):
        self.dataInitTialType = dataInitType
        self.dataInitial = dataInit # list of Point
        self.size = len(dataInit)
        self.k = k
        self.listLabel = label
        self.numOfLabel = len(set(label))
        self.distanceType = dType #1 euclid, 2 cosine..
        self.listDistances = []

        self.labelPercent = []

        self.fileDir = './' + dataName
        self.outfileDir = './outfile/' + dataName + '/knn_vectorinput/'
        if dataInitType == DATASETS_IS_TEXT:
            self.outfileDir = './outfile/' + dataName + '/knn_textinput/'
        self.fileName = dataName
    
    def predict(self, newPoint: Point):
        for point in self.dataInitial:
            self.listDistances.append(newPoint.euclid_distance(point))
        (self.listDistances, self.listLabel) = zip(*sorted(zip(self.listDistances, self.listLabel)))
        self.write_distance()
        self.listDistances = list(self.listDistances)
        self.listLabel = list(self.listLabel)
        # get top k in dataInit
        labelCount = [] # counting follow index
        for iLabel in range(self.numOfLabel):
            labelCount.append(self.listLabel[:int(self.k)].count(iLabel))
        for count in labelCount:
            self.labelPercent.append(round((count / sum(labelCount))*100, 2))
        self.write_predict()
        
    def write_predict(self):
        predict = []
        for i in range(self.numOfLabel):
            predict.append('{0} : {1}'.format(i, self.labelPercent[i]))
        write_file.list_to_txt(predict, './outfile/' + self.fileName + '/', 'predict.out')

    def write_distance(self):
        sortDisLabel = []
        for i in range(self.size):
            sortDisLabel.append('{0} : {1}'.format(self.listDistances[i], self.listLabel[i]))
        write_file.list_to_txt(sortDisLabel, './outfile/' + self.fileName + '/', 'distance_sorted.txt')


def main():
    linkDatasets = './datasets'
    # fileName = 'giao_thong.txt'
    # fileName = 'giao_thong.txt_list_sent_labeled.txt'
    fileName = 'BTTrongLop.vector'
    fileLabel = 'BTTrongLop.vector_labeled.lb'
    ### KNN
    datasetsVect = read_file.read_lines_to_listPoint(linkDatasets, fileName, ', ')
    labels = read_file.read_lines_to_intlist(linkDatasets, fileLabel, ', ')
    knn = KNearestNeighbor(DATASETS_IS_VECTOR, datasetsVect, 3, labels, 1, fileName)
    knn.predict(Point([6, 6]))
    

if __name__ == '__main__': main()