from Point import Point
from FUNC_working_with_file import read_file, write_file, make_folder
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
        self.numOfLabel = len(label)
        self.distanceType = dType #1 euclid, 2 cosine..
        self.listDistances = []

        self.labelPercent = {}
        self.dataInitSorted = []
        self.labelCount = {}

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
            distances.append(newPoint.euclid_distance(point))
        indexSorted = list(range(len(self.dataInitial)))
        (distances, labels, indexSorted) = zip(*sorted(zip(distances, labels, indexSorted)))
        self.write_distance(distances, labels)
        self.write_dataInitSorted(indexSorted)
        distances = list(distances)
        labels = list(labels)
        # get top k in dataInit
        labelSorted = []
        for i in range(self.k):
            labelSorted.append(labels[i])
        self.labelCount = {}
        for l in labelSorted:
            if l not in self.labelCount:
                self.labelCount[l] = 1
            else:
                self.labelCount[l] += 1
        self.labelPercent = {}
        for (label, count) in self.labelCount.items():
            self.labelPercent[label] = round((count / self.k)*100, 2)
        # self.write_predict(newPoint.display())
        
    def write_dataInitSorted(self, indexSorted: list):
        write_file.list_to_txt(indexSorted, 'outfile', 'index_ascending', '.txt', ', ')
    
    def write_predict(self, newStr: str):
        predict = []
        predict.append(newStr)
        for (label,percent) in self.labelPercent.items():
            predict.append('{0} : {1}'.format(label, percent))
        write_file.list_to_txt(predict, 'outfile', 'predict', '.out', '\n')

    def write_distance(self, distances: list, labels: list):
        sortDisLabel = []
        # for i in range(self.size): # all distance
        for i in range(self.k): # top k distance
            sortDisLabel.append('{0} : {1}'.format(distances[i], labels[i]))
        write_file.list_to_txt(sortDisLabel, 'outfile', 'distance_ascending', '.txt', '\n')

def main():
    folderName = 'datasets'
    fileName = 'BTTrongLop'
    fileType = ['.txt', '.vector', '.lb', '.vtest', '.vtested']
    ### KNN
    k = 3
    distanceType = 1
    # datasetsVect = read_file.read_lines_to_listPoint(linkDatasets, fileName + '.vector', ', ')
    listVect = read_file.read_lineSplited_to_list(folderName, fileName, fileType[1], ', ', 1)
    datasetsVect = [Point(vect) for vect in listVect]
    labels = read_file.read_lineSplited_to_list(folderName, fileName, fileType[2], ', ', 1)
    knn = KNearestNeighbor(DATASETS_IS_VECTOR, datasetsVect, k, labels, distanceType, fileName)
    knn.predict(Point([1, 6]))
    knn.write_predict(Point([1, 6]).display())
    # read file
    # vecTest = read_file.read_lineSplited_to_list(folderName, fileName, fileType[3], '\n', 1)
    # # vect to point
    # points = [Point(vec) for vec in vecTest]
    # # knn.predict_a_file(points, 5)
    # listResult = []
    # for p in points:
    #     knn.predict(p)
    #     listResult.append(p.display())
    #     listResult.append(str(knn.labelPercent))
    
    # write_file.list_to_txt(listResult, 'outfile', fileName, fileType[4], '\n')
    

if __name__ == '__main__': main()