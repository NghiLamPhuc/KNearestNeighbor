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
        self.k = int(k)
        self.listLabel = label
        self.numOfLabel = len(set(label))
        self.distanceType = dType #1 euclid, 2 cosine..
        self.listDistances = []

        self.labelPercent = []
        self.dataInitSorted = []

        self.fileDir = './' + dataName
        self.outfileDir = './outfile/' + dataName + '/knn_vectorinput/'
        if dataInitType == DATASETS_IS_TEXT:
            self.outfileDir = './outfile/' + dataName + '/knn_textinput/'
        self.fileName = dataName
    
    def predict(self, newPoint: Point):
        distances = []
        labels = self.listLabel.copy()
        indexSorted = []

        for point in self.dataInitial:
            # self.listDistances.append(newPoint.euclid_distance(point))
            distances.append(newPoint.euclid_distance(point))
        # self.dataInitSorted = list(range(len(self.dataInitial)))
        indexSorted = list(range(len(self.dataInitial)))
        # (self.listDistances, self.listLabel, self.dataInitSorted) = zip(*sorted(zip(self.listDistances, self.listLabel, self.dataInitSorted)))
        (distances, labels, indexSorted) = zip(*sorted(zip(distances, labels, indexSorted)))
        self.write_distance(distances, labels)
        self.write_dataInitSorted(indexSorted)
        # self.listDistances = list(self.listDistances)
        # self.listLabel = list(self.listLabel)
        distances = list(distances)
        labels = list(labels)
        # get top k in dataInit
        labelCount = [] # counting follow index
        for iLabel in range(self.numOfLabel):
            # labelCount.append(self.listLabel[:self.k].count(iLabel))
            labelCount.append(labels[:self.k].count(iLabel))
        self.labelPercent = []
        for count in labelCount:
            self.labelPercent.append(round((count / sum(labelCount))*100, 2))
        # self.write_predict(newPoint.display())
        
    def write_dataInitSorted(self, indexSorted: list):
        write_file.list_to_txt(indexSorted, './outfile/' + self.fileName + '/', 'index_ascending.txt')
    
    def write_predict(self, newStr: str):
        predict = []
        predict.append(newStr)
        for i in range(self.numOfLabel):
            predict.append('{0} : {1}'.format(i, self.labelPercent[i]))
        write_file.list_to_txt(predict, './outfile/' + self.fileName + '/', 'predict.out')

    def write_distance(self, distances: list, labels: list):
        sortDisLabel = []
        # for i in range(self.size): # all distance
        for i in range(self.k): # top k distance
            sortDisLabel.append('{0} : {1}'.format(distances[i], labels[i]))
        write_file.list_to_txt(sortDisLabel, './outfile/' + self.fileName + '/', 'distance_ascending.txt')

    # a file == list of points
    # def predict_a_file(self, points: list, k: int):
    #     listResult = []
    #     for p in points:
    #         knn.predict(p)
    #         listResult.append(p.display())
    #         listResult.append(str(knn.labelPercent))
        
    #     write_file.list_to_txt(listResult, './outfile/' + fileName + '/', fileName + '.tested')


def main():
    linkDatasets = './datasets'
    fileName = 'BTTrongLop'
    ### KNN
    k = 3
    distanceType = 1
    datasetsVect = read_file.read_lines_to_listPoint(linkDatasets, fileName + '.vector', ', ')
    labels = read_file.read_lines_to_intlist(linkDatasets, fileName + '.lb', ', ')
    knn = KNearestNeighbor(DATASETS_IS_VECTOR, datasetsVect, k, labels, distanceType, fileName)
    # knn.predict(Point([1, 6]))
    # read file
    vecs = read_file.read_lines_to_floatlist(linkDatasets, fileName + '.vtest', ', ')
    # vect to point
    points = [Point(vec) for vec in vecs]
    # knn.predict_a_file(points, 5)
    listResult = []
    for p in points:
        knn.predict(p)
        listResult.append(p.display())
        listResult.append(str(knn.labelPercent))
    
    write_file.list_to_txt(listResult, './outfile/' + fileName + '/', fileName + '.tested')
    

if __name__ == '__main__': main()