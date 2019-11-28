from PyQt5 import QtCore, QtGui, QtWidgets, uic
import read_file, write_file, make_folder
from KNearestNeighborClass import KNearestNeighbor
from Point import Point
from gensim.models import Word2Vec
from sentence2vec import Sentence2Vec
from underthesea import word_tokenize
from datetime import datetime, timedelta
import re
import sys

DATASETS_IS_VECTOR = 1
DATASETS_IS_TEXT = 0

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('GUI.ui', self)

        imgDir = './GUIimage/'
        openIcon = QtGui.QIcon(imgDir + 'openIcon')
        saveIcon = QtGui.QIcon(imgDir + 'saveIcon')
        runIcon = QtGui.QIcon(imgDir + 'runIcon')
        resIcon = QtGui.QIcon(imgDir + 'saveResIcon')
        pixmapLogo = QtGui.QPixmap(imgDir + 'logoIconLarge')
        vectorIcon = QtGui.QIcon(imgDir + 'vectorIcon')
        kNNsIcon = QtGui.QIcon(imgDir + 'kNNsIcon')
        
        self.btnImport.setIcon(openIcon)
        self.btnExport.setIcon(saveIcon)
        self.btnKNN.setIcon(runIcon)
        self.btnVectorize.setIcon(vectorIcon)
        self.btnKNNFile.setIcon(kNNsIcon)
        self.labelLogo.setPixmap(pixmapLogo)
        
        self.btnVectorize.clicked.connect(self.on_Vectorize_clicked)
        self.btnKNN.clicked.connect(self.on_KNN_clicked)
        self.btnImport.clicked.connect(self.on_Import_clicked)
        self.btnExport.clicked.connect(self.on_Export_clicked)
        # self.btnScreenShot.clicked.connect(self.on_ScreenShot_clicked)
        self.btnKNNFile.clicked.connect(self.on_KNNFile_clicked)

        self.spinBoxK.setValue(2)
        self.spinBoxVecSize.setValue(100)
        self.lineEditPredict.textChanged.connect(self.on_text_predict_changed)

        self.groupBoxVectorize.setEnabled(False)
        self.groupBoxKNN.setEnabled(False)
        self.btnExport.setEnabled(False) ############################# Sau này thêm chức năng.
        self.labelInputName.setText('Dữ liệu')
        self.lineEditPredict.setEnabled(False)
        
        self.listRawSents = list()
        self.listSentToWord = list()
        self.initData = None
        self.inputDir = './datasets'
        self.fileInitName = None
        self.checkKNN = 0
        self.kNN = None
        self.listLabel = list()
        # 0, 1 sau này đưa về kiểu biến Str = 0 / 1
        self.checkVectorize = 0 # 0 khi chưa vector hóa, 1 khi vector hóa rồi.
        self.checkDataType = 0 # 0 khi Dữ liệu là text, 1 khi dữ liệu là vector.
    
    # def on_ScreenShot_clicked(self):
    #     screen = QtWidgets.QApplication.primaryScreen()
    #     screenshot = screen.grabWindow( QtWidgets.QWidget.winId() )
    #     screenshot.save('shot.jpg', 'jpg')
    #     QtWidgets.QWidget.close()

    def on_Vectorize_clicked(self):
        start = datetime.now()
        vectorSize = int(self.spinBoxVecSize.text())
        if len(self.listRawSents) == 0:
            self.labelLog.setText('Chưa có câu.')
        else:
            linkFolder = 'outfile/{0}'.format(self.fileInitName)
            make_folder.create_folder(linkFolder)
            linkModel = linkFolder + '/word2vec.model'
            # token sentences --> to list
            for sent in self.listRawSents:
                tokens = word_tokenize(sent, format='text').split()
                words = []
                for token in tokens:
                    if re.match(r'^\w+', token):
                        words.append(token)
                self.listSentToWord.append(words)
            # training word2vec cho cái list tách từ.
            model = Word2Vec(self.listSentToWord, size=vectorSize, window=5, sg=1, min_count=5, workers=5)
            model.save(linkModel)
            sent2vec = Sentence2Vec(linkModel)
            listVect = []
            for sent in self.listRawSents:
                listVect.append(sent2vec.get_vector(sent).tolist())
            write_file.list_to_txt(listVect, linkFolder, 'Sent2Vect.txt')
            write_file.list_to_txt(self.listSentToWord, linkFolder, 'WordTokenize.txt')

            self.checkVectorize = 1
            self.groupBoxKNN.setEnabled(True)
            self.lineEditPredict.setEnabled(True)
        exeTime = (datetime.now() - start).total_seconds()
        self.labelLog.setText('Đã lưu file vector. \t{0}'.format(str(timedelta(seconds = exeTime))))
            
            
    def on_text_predict_changed(self):
        self.labelLog.clear()

    def on_Export_clicked(self):
        inputDir = './datasets/'
        (dataPath, _) = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', inputDir, '*.txt')
        if dataPath:
            data = self.plainTextInput.toPlainText()
            with open(dataPath, 'w', encoding = 'utf-8') as f:
                f.write(data)

    def on_Import_clicked(self):
        self.labelLog.clear()
        self.labelInput.clear()
        self.plainTextInput.clear()
        self.lineEditPredict.clear()
        self.groupBoxVectorize.setEnabled(False)
        self.groupBoxKNN.setEnabled(False)
        self.lineEditPredict.clear()
        self.lineEditPredict.setEnabled(False)
        self.btnKNNFile.setEnabled(False)
        self.checkDataType = DATASETS_IS_TEXT #0
        if self.radioVector.isChecked():
            self.checkDataType = DATASETS_IS_VECTOR#1
        
        self.checkVectorize = 0
        if self.radioVector.isChecked():
            self.checkDataType = 1
        
        # ###################################### input la text
        if self.checkDataType == DATASETS_IS_TEXT:
            (dataPath, _) = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', self.inputDir, '*.txt')
            self.fileInitName = ''.join(list(dataPath.split('/')[-1])[:-4])
            if dataPath:
                # câu thô.
                self.listLabel = read_file.read_lines_to_intlist(self.inputDir, self.fileInitName + '.lb', ', ')
                
                self.listRawSents = read_file.read_line_to_sentenceList(self.inputDir, self.fileInitName + '.txt', '\n')
                rowCount = len(self.listRawSents)
                for i in range(rowCount):
                    rowStr = '[{0}]. {1} : {2}\n'.format(i, self.listRawSents[i], self.listLabel[i])
                    self.plainTextInput.insertPlainText(rowStr)

                self.labelInput.setText('Có {} dòng.'.format(rowCount) )
                self.labelInputName.setText(self.fileInitName)
                self.spinBoxK.setMaximum(rowCount)

                self.groupBoxVectorize.setEnabled(True)
            else:
                self.lineEditPredict.setPlaceholderText('')

        # #################################### input la vector
        elif self.checkDataType == DATASETS_IS_VECTOR:
            (dataPath, _) = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', self.inputDir, '*.vector')
            self.fileInitName = ''.join(list(dataPath.split('/')[-1])[:-7])
            if dataPath:
                # data đã số hóa.
                self.listLabel = read_file.read_lines_to_intlist(self.inputDir, self.fileInitName + '.lb', ', ')

                listVect = read_file.read_lines_to_floatlist(self.inputDir, self.fileInitName + '.vector', ', ' )
                toPoints = []
                for vec in listVect:
                    toPoints.append(Point(vec))
                self.initData = toPoints

                rowCount = len(self.initData)
                for (i, row) in enumerate(self.initData):
                    rowStr = '[{0}]. {1} : {2}\n'.format(i, row.display(), self.listLabel[i])
                    self.plainTextInput.insertPlainText(rowStr)
                
                self.labelInput.setText('Có {} dòng.'.format(rowCount) )
                self.labelInputName.setText(self.fileInitName)
                self.spinBoxK.setMaximum(rowCount)

                self.groupBoxKNN.setEnabled(True)
                self.lineEditPredict.setEnabled(True)
                hint = 'Nhập tọa độ vector.'
                self.lineEditPredict.setPlaceholderText(hint)
            else:
                self.lineEditPredict.setPlaceholderText('')
    
    def on_KNN_clicked(self):
        start = datetime.now()
        k = int(self.spinBoxK.text())
        ##################################### neu input la text
        if self.checkDataType == DATASETS_IS_TEXT:
            # đọc initData từ Sent2Vect.txt
            sent2vect = read_file.read_lines_to_floatlist('./outfile/{0}/'.format(self.fileInitName), 'Sent2Vect.txt', ', ' )
            toPoints = []
            for vec in sent2vect:
                toPoints.append(Point(vec))
            self.initData = toPoints
        
        dType = 1
        # if self.radioButtonCosine.isChecked():
        #     dType = 2
        
        self.kNN = KNearestNeighbor(self.checkDataType, self.initData, k, self.listLabel, dType, self.fileInitName)
        
        ######################## input la vector
        self.checkKNN = 1
        
        ## Predict new from lineEditPredict
        newSent = self.lineEditPredict.text()
        
        if self.checkDataType == DATASETS_IS_TEXT:
            if not newSent:
                self.labelLog.setText('Chưa nhập câu.')
            elif self.checkKNN == 0:
                self.labelLog.setText('Chưa phân lớp.')
            else:
                linkModel = './outfile/{0}/word2vec.model'.format(self.fileInitName)
                sent2vec = Sentence2Vec(linkModel)
                vecSentList = sent2vec.get_vector(newSent).tolist()
                newPoint = Point(vecSentList)
                self.kNN.predict(newPoint)
                self.kNN.write_predict(newSent)
                exeTime = (datetime.now() - start).total_seconds()
                self.labelLog.setText('{0} \t{1}'.format(self.kNN.labelPercent, str(timedelta(seconds = exeTime))))
        elif self.checkDataType == DATASETS_IS_VECTOR:
            if not newSent:
                self.labelLog.setText('Chưa nhập vector.')
            elif self.checkKNN == 0:
                self.labelLog.setText('Chưa phân lớp.')
            else:
                coordList = list()
                for coord in newSent.split(','):
                    coordList.append(float(coord))
                newPoint = Point(coordList)
                self.kNN.predict(newPoint)
                self.kNN.write_predict(newPoint.display())
                exeTime = (datetime.now() - start).total_seconds()
                self.labelLog.setText('{0} \t{1}'.format(self.kNN.labelPercent, str(timedelta(seconds = exeTime))))
        self.btnKNNFile.setEnabled(True)
           
    def on_KNNFile_clicked(self):
        start = datetime.now()
        self.plainTextInput.clear()
        '''
        Read file (vtest: vector test; ttest: text test)
        if vtest:
            for vec in file:
                list append(predict(vec))
        if ttest:
            for sent in file:
                load word2vec model
                sent -> sent2vec
                list append(predict(Point(sent2vec)))
        '''
        if self.checkDataType == DATASETS_IS_VECTOR:
            (dataPath, _) = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', self.inputDir, '*.vtest')
            self.fileInitName = ''.join(list(dataPath.split('/')[-1])[:-6])
            if dataPath:
                listVect = read_file.read_lines_to_floatlist(self.inputDir, self.fileInitName + '.vtest', ', ')
                toPoints = []
                for vec in listVect:
                    toPoints.append(Point(vec))
                
                rowCount = len(listVect)
                for (i, row) in enumerate(toPoints):
                    rowStr = '[{0}]. {1}\n'.format(i, row.display())
                    self.plainTextInput.insertPlainText(rowStr)
            
                self.labelInput.setText('Có {} dòng.'.format(rowCount) )
                self.labelInputName.setText(self.fileInitName)
                # need predict this toPoints
                listResult = []
                for p in toPoints:
                    self.kNN.predict(p)
                    listResult.append(p.display())
                    listResult.append(str(self.kNN.labelPercent))
                write_file.list_to_txt(listResult, './outfile/' + self.fileInitName + '/', self.fileInitName + '.tested')
                exeTime = (datetime.now() - start).total_seconds()
                self.labelLog.setText('Đã gán xong! \t{0}'.format(str(timedelta(seconds = exeTime))))
        elif self.checkDataType == DATASETS_IS_TEXT:
            (dataPath, _) = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', self.inputDir, '*.ttest')
            self.fileInitName = ''.join(list(dataPath.split('/')[-1])[:-6])
            if dataPath:
                # sentence câu thô
                listRawSents = read_file.read_line_to_sentenceList(self.inputDir, self.fileInitName + '.ttest', '\n')
                rowCount = len(listRawSents)
                for i in range(rowCount):
                    rowStr = '[{0}]. {1}\n'.format(i, listRawSents[i])
                    self.plainTextInput.insertPlainText(rowStr)
                
                self.labelInput.setText('Có {} dòng.'.format(rowCount) )
                self.labelInputName.setText(self.fileInitName)
                # load word2vecmodel set sent2vec
                linkFolder = 'outfile/{0}'.format(self.fileInitName)
                linkModel = linkFolder + '/word2vec.model'
                sent2vec = Sentence2Vec(linkModel)
                listVect = []
                for sent in listRawSents:
                    listVect.append(sent2vec.get_vector(sent).tolist())
                write_file.list_to_txt(listVect, linkFolder, self.fileInitName + 'New_Sent2Vect.txt')
                # predict
                newSent2vec = read_file.read_lines_to_floatlist('./outfile/{0}/'.format(self.fileInitName), self.fileInitName + 'New_Sent2Vect.txt', ', ')

                toPoints = []
                for vec in newSent2vec:
                    toPoints.append(Point(vec))
                
                listResult = []
                for p in toPoints:
                    self.kNN.predict(p)
                    listResult.append(p.display())
                    listResult.append(str(self.kNN.labelPercent))
                
                write_file.list_to_txt(listResult, './outfile/' + self.fileInitName + '/', self.fileInitName + '.tested')
                exeTime = (datetime.now() - start).total_seconds()
                self.labelLog.setText('Đã gán xong! \t{0}'.format(str(timedelta(seconds = exeTime))))
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow()
    window.setWindowTitle('K Nearest Neighbor')
    window.show()
    sys.exit(app.exec_())

