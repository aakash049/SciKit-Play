import os

import numpy as np
from PIL import Image
from sklearn import cross_validation
from sklearn import svm
from sklearn.externals import joblib

from utils import *


class CellRecognizer:
    def __init__(self):
        self.trainingData = []
        self.targetValues = []
        self.svc = svm.SVC(gamma=0.001, kernel="linear", C=100)
        self.down_res = (32, 32)

    def _load(self, path, target_value):
        training_imgs = os.listdir(path)
        for f in training_imgs:
            img = Image.open(path + "/" + f)
            img = img.resize(self.down_res, Image.BILINEAR)
            self.trainingData.append(np.array(img.getdata()).flatten())
            self.targetValues.append(target_value)

    def load(self):
        pt = 'Training_Data/Cells'
        self._load(pt + '/Blue', blue)
        self._load(pt + '/Blue_Striped_H', blue_s_h)
        self._load(pt + '/Blue_Striped_V', blue_s_v)
        self._load(pt + '/Blue_Wrapped', blue_w)
        self._load(pt + '/Green', green)
        self._load(pt + '/Green_Striped_H', green_s_h)
        self._load(pt + '/Green_Striped_V', green_s_v)
        self._load(pt + '/Green_Wrapped', green_w)
        self._load(pt + '/Orange', orange)
        self._load(pt + '/Orange_Striped_H', orange_s_h)
        self._load(pt + '/Orange_Striped_V', orange_s_v)
        self._load(pt + '/Orange_Wrapped', orange_w)
        self._load(pt + '/Purple', purple)
        self._load(pt + '/Purple_Striped_H', purple_s_h)
        self._load(pt + '/Purple_Striped_V', purple_s_v)
        self._load(pt + '/Purple_Wrapped', purple_w)
        self._load(pt + '/Red', red)
        self._load(pt + '/Red_Striped_H', red_s_h)
        self._load(pt + '/Red_Striped_V', red_s_v)
        self._load(pt + '/Red_Wrapped', red_w)
        self._load(pt + '/Yellow', yellow)
        self._load(pt + '/Yellow_Striped_H', yellow_s_h)
        self._load(pt + '/Yellow_Striped_V', yellow_s_v)
        self._load(pt + '/Yellow_Wrapped', yellow_w)
        self._load(pt + '/Chocolate', chocolate_c)

    # import training data to scikit if it already exists
    # else, train the bot with the sample data
    def train(self):
        folder = 'cell_dat'
        pt = os.getcwd() + '/' + folder
        if os.path.isdir(folder):
            dat = os.listdir(pt)
            if not int(len(dat)) == 0:
                self.svc = joblib.load(pt + '/' + cell_recognizer)
            else:
                self.learn_dat(pt)
        else:
            os.mkdir(pt)
            self.learn_dat(pt)

    def learn_dat(self, path):
        self.load()
        np_data = np.array(self.trainingData)
        np_values = np.array(self.targetValues)
        self.svc.fit(np_data, np_values)
        joblib.dump(self.svc, path + '/' + cell_recognizer)

    def test(self):
        np_train_data = np.array(self.trainingData)
        np_values = np.array(self.targetValues)
        data, test_data, train_target, test_target = \
            cross_validation.train_test_split(np_train_data, np_values, test_size=0.4, random_state=0)
        self.svc.fit(data, train_target)
        print self.svc.score(test_data, test_target)

    def predict(self, img):
        resized_img = img.resize(self.down_res, Image.BILINEAR)
        np_img = np.array(resized_img.getdata()).flatten()
        return int(self.svc.predict(np_img))
