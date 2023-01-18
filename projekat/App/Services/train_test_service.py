from Repository.dataset_repository import DatasetRepository
from Services.preparer_service import PreparerService
from Services.ann_regression import AnnRegression
from Services.scorer import Scorer
import datetime
import pandas as pd
import numpy as np
import os
import time

SHARE_FOR_TRAINING = 0.90

class TrainTestService:
    def __init__(self):
        self.datasetRepository = DatasetRepository()

    def TrainModel(self, date1, date2):
        if date1 == "Chose date..." and date2 != "Chose date...":
            df = self.datasetRepository.readTrainDataFromDatabase("'2018-01-01 00:00:00'", "'2021-09-06 23:00:00'")
        else:
            date_1 = pd.to_datetime(date1)
            date_2 = pd.to_datetime(date2)
            if date_1 > date_2:
                return False
            else:
                date1 = date1.replace("/", "-")
                date1 += " 00:00:00"
                date1 = "'%s'" %(date1)
                date2 = date2.replace("/", "-")
                date2 += " 23:00:00"
                date2 = "'%s'" % (date2)
                df = self.datasetRepository.readTrainDataFromDatabase(date1, date2)
                print(df.head())
        self.preparerService = PreparerService(df, SHARE_FOR_TRAINING)
        trainX, trainY, testX, testY = self.preparerService.prepare_for_training()

        ann_regression = AnnRegression()
        time_begin = time.time()
        trainPredict, testPredict = ann_regression.compile_fit_predict(trainX, trainY, testX)
        time_end = time.time()
        print('Training duration: ' + str((time_end - time_begin)) + ' seconds')

        trainPredict, trainY, testPredict, testY = self.preparerService.inverse_transform(trainPredict, testPredict)

        scorer = Scorer()
        trainScore, testScore = scorer.get_score(trainY, trainPredict, testY, testPredict)
        print(trainY)
        print(trainPredict)
        print('Train Score: %.2f RMSE' % (trainScore))
        print('Test Score: %.2f RMSE' % (testScore))

        return testPredict, testY

        # df = self.datasetRepository.readTrainDataFromDatabase("'2018-01-01 00:00:00'", "'2021-09-06 23:00:00'")
        # print(df.tail(5))
        # print(len(df.index))

    def predictLoad(self, date, num_days):
        pass

    def GetDatetime(self, date1, date2):
        if date1 == "Chose date..." and date2 != "Chose date...":
            df = self.datasetRepository.readDateTimeForPredict("'2018-01-01 00:00:00'", "'2021-09-06 23:00:00'")
            return df
        else:
            date_1 = pd.to_datetime(date1)
            date_2 = pd.to_datetime(date2)
            if date_1 > date_2:
                return False
            else:
                date1 = date1.replace("/", "-")
                date1 += " 00:00:00"
                date1 = "'%s'" %(date1)
                date2 = date2.replace("/", "-")
                date2 += " 23:00:00"
                date2 = "'%s'" % (date2)
                df = self.datasetRepository.readDateTimeForPredict(date1, date2)
                return df