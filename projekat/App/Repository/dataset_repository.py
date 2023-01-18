from sqlalchemy import create_engine
import pymysql
import pandas as pd

DB_CONNECTION_STR = 'mysql+pymysql://root:root@localhost/isisdatabase'
TABLE_NAME = "dataset"


class DatasetRepository:
    def __init__(self):
        sqlEngine = create_engine(DB_CONNECTION_STR)
        self.dbConnection = sqlEngine.connect()

    def closeConnection(self):
        self.dbConnection.close()

    def writeIntoDatabase(self, dataFrame):
        try:
            frame = dataFrame.to_sql(TABLE_NAME, self.dbConnection, if_exists='append');
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Table %s created successfully." % TABLE_NAME);

    def readAllFromDatabase(self):
        frame = pd.read_sql("select * from " + TABLE_NAME, self.dbConnection);
        return frame

    def readTrainDataFromDatabase(self, first_date, second_date):
        frame = pd.read_sql("select datetime, temp, feelslike, dew, humidity, windspeed, cloudcover, `Load`  from " + TABLE_NAME + " where datetime between " + first_date + " and " + second_date, self.dbConnection);
        return frame

    def readDateTimeForPredict(self, first_date, second_date):
        frame = pd.read_sql("select datetime from " + TABLE_NAME + " where datetime between " + first_date + " and " + second_date, self.dbConnection);
        return frame
