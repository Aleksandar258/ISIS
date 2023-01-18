from Repository.dataset_repository import DatasetRepository
import datetime
import pandas as pd
import numpy as np
import os
import glob
import math


class DatasetService:
    def __init__(self):
        self.holidays = self.loadHolidays()
        self.datasetRepository = DatasetRepository()

    def loadCSVFolder(self, folder):
        pathWeatherData = folder + "/NYS Weather Data/New York City, NY"
        weather_csv_files = glob.glob(os.path.join(pathWeatherData, "*.csv"))

        pathLoadData = folder + "/NYS Load  Data"
        list_load_folders = []
        for f in os.listdir(pathLoadData):
            d = os.path.join(pathLoadData, f)
            if os.path.isdir(d):
                list_load_folders.append(d)

        br = 0
        for wf in weather_csv_files:
            df_weather_file = pd.read_csv(wf)
            # print(df_weather_file.iloc[[0]])
            df_weather_file = self.populateMissingWeatherValues(df_weather_file)
            # print("cloudcover: ", df_weather_file["cloudcover"].isna().sum())
            # # print("dew2: ", df_weather_file["dew"].isna())
            # br = 0
            # for b in df_weather_file["winddir"].isna():
            #     if b == True:
            #         print(br)
            #     br += 1
            # print("visibility: ", df_weather_file["visibility"].isna().sum())
            # print("conditions: ", df_weather_file["conditions"].isna().sum())
            # print("winddir: ", df_weather_file["winddir"].isna().sum())
            # pd.set_option('display.max_columns', None)
            # print(df_weather_file.head(10))
            load_during_the_year = []
            ptid_during_the_year = []
            first_time = True
            load_copy = []
            for j in range(12):
                if br == 3 and j == 9:
                    break
                # if br == 3 and j == 3:
                #     for l in range(168):
                #         load_during_the_year.append(0)
                load_csv_files = glob.glob(os.path.join(list_load_folders[br * 12 + j], "*.csv"))
                for lf in load_csv_files:
                    df_load_file = pd.read_csv(lf)
                    br_load_unpopulated = 0
                    past_load = 0
                    for i, row in df_load_file.iterrows():
                        date_time = row["Time Stamp"].split(' ')
                        m_d_y = date_time[0].split('/')
                        time = date_time[1]
                        min_and_sec = time.split(':')
                        if min_and_sec[1] == '00' and min_and_sec[2] == '00' and row["Name"] == "N.Y.C.":
                            if br == 3 and j == 3 and int(m_d_y[1]) <= 14:
                                load_copy.append(row["Load"])
                                load_during_the_year.append((row["Load"] + load_during_the_year[len(load_during_the_year) - 7 * 24]) / 2)
                            elif br == 3 and j == 3 and int(m_d_y[1]) == 15 and first_time:
                                for e in load_copy:
                                    load_during_the_year.append(e)
                                load_during_the_year.append(row["Load"])
                                first_time = False
                            else:
                                if pd.isnull(row["Load"]):
                                    br_load_unpopulated += 1
                                else:
                                    if br_load_unpopulated > 0:
                                        value = round((past_load + row["Load"]) / 2, 2)
                                        for p in range(br_load_unpopulated):
                                            load_during_the_year.append(value)
                                        br_load_unpopulated = 0
                                    load_during_the_year.append(row["Load"])
                                    past_load = row["Load"]
                            # if br == 3 and j == 2 and int(m_d_y[1]) >= 25 and int(m_d_y[1]) <= 31:
                            #     load_copy.append(row["Load"])
                            # ptid_during_the_year.append(row["PTID"])
            # df_weather_file["PTID"] = ptid_during_the_year
            df_weather_file["Load"] = load_during_the_year
            df_weather_file["datetime"] = pd.to_datetime(df_weather_file["datetime"])
            print("conditions:", df_weather_file["Load"].isna().sum())
            self.datasetRepository.writeIntoDatabase(df_weather_file)
            print("df: ", len(df_weather_file.index))
            print("Load: ", len(load_during_the_year))
            br += 1
            # print(df_weather_file.head())
            pd.set_option('display.max_columns', None)
            print(df_weather_file.head(10))

        print("------------------FINISHED--------------------")


    def getDatesFromDatabase(self):
        df = self.datasetRepository.readAllFromDatabase()
        print(df.head())
        dates_col = df["datetime"].dt.date.unique()
        dates = dates_col.tolist()
        dates = [date_obj.strftime('%Y/%m/%d') for date_obj in dates]
        return dates


            # print('Location:', f)
            # print('File Name:', f.split("\\")[-1])

    def populateMissingWeatherValues(self, df):
        a = pd.isnull(df.iloc[0, 12])
        print("--------conditions:", a, "-------")
        # print("conditions:", df["dew"].isna().sum())
        br_row_unpopulated = {"feelslike": 0, "dew": 0,"humidity": 0,"precip": 0,"windgust": 0,"windspeed": 0,"winddir": 0,"sealevelpressure": 0,"cloudcover": 0,"visibility": 0,"solarradiation": 0,"solarenergy": 0,"severerisk": 0,"conditions": 0}
        past_values = {"feelslike": 0, "dew": 0, "humidity": 0, "precip": 0, "windgust": 0, "windspeed": 0,
                              "winddir": 0, "sealevelpressure": 0, "cloudcover": 0, "visibility": 0,
                              "solarradiation": 0, "solarenergy": 0, "severerisk": 0, "conditions": 0}
        for i, row in df.iterrows():
            # print(i)
            list_of_ex_values = pd.isnull(row)
            # for j in range(16):
                # 3 - feelslike| 4 - dew| 5 - humidity| 6 - precip| 11 - windgust| 12 - windspeed| 13 - winddir| 14 - sealevelpressure| 15 - cloudcover|
                # 16 - visibility| 17 - solarradiation| 18 - solarenergy| 20 - severerisk| 21 - conditions

            #---------------------HUMIDITY-------------------------------------------
            if(list_of_ex_values[5] == True):
                if(list_of_ex_values[4] == False):
                    value = self.calculateHumidity(row["temp"], row["dew"])
                    df.iloc[i, 5] = value
                    row["humidity"] = value
                    past_values["humidity"] = value
                    if br_row_unpopulated["humidity"] > 0:
                        br_row_unpopulated["humidity"] -= 1
                else:
                    if br_row_unpopulated["humidity"] > 0:
                        row["humidity"] = past_values["humidity"]
                        df.iloc[i, 5] = past_values["humidity"]
                        br_row_unpopulated["humidity"] -= 1
                    else:
                        br_row_unpopulated["humidity"] = 0
                        for k in range(len(df.index) - i - 1):
                            if pd.isnull(df.iloc[i + k + 1, 5])== False:
                                value = round((past_values["humidity"] + df.iloc[i + k + 1, 5]) / 2, 2)
                                past_values["humidity"] = value
                                df.iloc[i, 5] = value
                                row["humidity"] = value
                                break
                            else:
                                br_row_unpopulated["humidity"] += 1
            else:
                past_values["humidity"] = row["humidity"]

            # ---------------------DEW-------------------------------------------
            if(list_of_ex_values[4] == True):
                temp = row["temp"]
                humidity = row["humidity"]
                value = self.calculateDew(temp, humidity)
                df.iloc[i, 4] = value
                row["dew"] = value

            # ---------------------WINDSPEED-------------------------------------------
            if (list_of_ex_values[12] == True):
                value = -1
                if(list_of_ex_values[3] == False):
                    temp = row["temp"]
                    feelslike = row["feelslike"]
                    value = self.calculateWindspeedFromFeelslike(temp, feelslike)
                    if value != -1:
                        df.iloc[i, 12] = value
                        row["windspeed"] = value
                        past_values["windspeed"] = value
                        if br_row_unpopulated["windspeed"] > 0:
                            br_row_unpopulated["windspeed"] -= 1
                if value == -1:
                    if br_row_unpopulated["windspeed"] > 0:
                        df.iloc[i, 12] = past_values["windspeed"]
                        row["windspeed"] = past_values["windspeed"]
                        br_row_unpopulated["windspeed"] -= 1
                    else:
                        br_row_unpopulated["windspeed"] = 0
                        for k in range(len(df.index) - i - 1):
                            if pd.isnull(df.iloc[i + k + 1, 12]) == False:
                                value = round((past_values["windspeed"] + df.iloc[i + k + 1, 12]) / 2, 1)
                                past_values["windspeed"] = value
                                df.iloc[i, 12] = value
                                row["windspeed"] = value
                                break
                            else:
                                br_row_unpopulated["windspeed"] += 1
            else:
                past_values["windspeed"] = row["windspeed"]

            # ---------------------FEELSLIKE-------------------------------------------
            if(list_of_ex_values[3] == True):
                value = self.calculateFeelslike(row["temp"], row["windspeed"], row["humidity"])
                row["feelslike"] = value
                df.iloc[i, 3] = value

            # ---------------------WINDGUST-------------------------------------------
            if (list_of_ex_values[11] == True):
                if br_row_unpopulated["windgust"] > 0:
                    df.iloc[i, 11] = past_values["windgust"]
                    row["windgust"] = past_values["windgust"]
                    # print("1row: ", i, ", value: ", past_values["windgust"], ", df.value: ", df.iloc[i, 11])
                    br_row_unpopulated["windgust"] -= 1
                else:
                    br_row_unpopulated["windgust"] = 0
                    for k in range(len(df.index) - i - 1):
                        if pd.isnull(df.iloc[i + k + 1, 11]) == False:
                            a = past_values["windgust"]
                            b = df.iloc[i + k + 1, 11]
                            value = round((past_values["windgust"] + df.iloc[i + k + 1, 11]) / 2, 1)
                            past_values["windgust"] = value
                            row["windgust"] = value
                            df.iloc[i, 11] = value
                            # print("2row: ", i, ", value: ", value, ", df.value: ", df.iloc[i, 11])
                            break
                        else:
                            br_row_unpopulated["windgust"] += 1
            else:
                past_values["windgust"] = row["windgust"]

            # ---------------------WINDDIR-------------------------------------------
            if (list_of_ex_values[13] == True):
                if br_row_unpopulated["winddir"] > 0:
                    df.iloc[i, 13] = past_values["winddir"]
                    row["winddir"] = past_values["winddir"]
                    br_row_unpopulated["winddir"] -= 1
                else:
                    br_row_unpopulated["winddir"] = 0
                    for k in range(len(df.index) - i - 1):
                        if pd.isnull(df.iloc[i + k + 1, 13]) == False:
                            value = round((past_values["winddir"] + df.iloc[i + k + 1, 13]) / 2, 1)
                            past_values["winddir"] = value
                            df.iloc[i, 13] = value
                            row["winddir"] = value
                            break
                        else:
                            br_row_unpopulated["winddir"] += 1
            else:
                past_values["winddir"] = row["winddir"]

            # ---------------------SEALEVELPRESSURE-------------------------------------------
            if (list_of_ex_values[14] == True):
                if br_row_unpopulated["sealevelpressure"] > 0:
                    df.iloc[i, 14] = past_values["sealevelpressure"]
                    row["sealevelpressure"] = past_values["sealevelpressure"]
                    br_row_unpopulated["sealevelpressure"] -= 1
                else:
                    br_row_unpopulated["sealevelpressure"] = 0
                    for k in range(len(df.index) - i - 1):
                        if pd.isnull(df.iloc[i + k + 1, 14]) == False:
                            value = round((past_values["sealevelpressure"] + df.iloc[i + k + 1, 14]) / 2, 1)
                            past_values["sealevelpressure"] = value
                            df.iloc[i, 14] = value
                            row["sealevelpressure"] = value
                            break
                        else:
                            br_row_unpopulated["sealevelpressure"] += 1
            else:
                past_values["sealevelpressure"] = row["sealevelpressure"]

            # ---------------------VISIBILITY-------------------------------------------
            if (list_of_ex_values[16] == True):
                if br_row_unpopulated["visibility"] > 0:
                    df.iloc[i, 16] = past_values["visibility"]
                    row["visibility"] = past_values["visibility"]
                    br_row_unpopulated["visibility"] -= 1
                else:
                    br_row_unpopulated["visibility"] = 0
                    for k in range(len(df.index) - i - 1):
                        if pd.isnull(df.iloc[i + k + 1, 16]) == False:
                            value = round((past_values["visibility"] + df.iloc[i + k + 1, 16]) / 2, 1)
                            past_values["visibility"] = value
                            df.iloc[i, 16] = value
                            row["visibility"] = value
                            break
                        else:
                            br_row_unpopulated["visibility"] += 1
            else:
                past_values["visibility"] = row["visibility"]

            # ---------------------PRECIP-------------------------------------------
            if (list_of_ex_values[6] == True):
                if (list_of_ex_values[21] == False):
                    conditions = row["conditions"]
                    value = 0
                    if "Rain" in conditions or "Snow" in conditions:
                        if past_values["precip"] > 0:
                            value = past_values["precip"]
                        else:
                            value = 0.10
                    else:
                        value = 0
                    df.iloc[i, 6] = value
                    row["precip"] = value
                    past_values["precip"] = value
                    if br_row_unpopulated["precip"] > 0:
                        br_row_unpopulated["precip"] -= 1
                else:
                    if br_row_unpopulated["precip"] > 0:
                        df.iloc[i, 6] = past_values["precip"]
                        row["precip"] = past_values["precip"]
                        br_row_unpopulated["precip"] -= 1
                    else:
                        br_row_unpopulated["precip"] = 0
                        for k in range(len(df.index) - i - 1):
                            if pd.isnull(df.iloc[i + k + 1, 6]) == False:
                                value = round((past_values["precip"] + df.iloc[i + k + 1, 6]) / 2, 2)
                                past_values["precip"] = value
                                df.iloc[i, 6] = value
                                row["precip"] = value
                                break
                            else:
                                br_row_unpopulated["precip"] += 1
            else:
                past_values["precip"] = row["precip"]

            # ---------------------CLOUDCOVER-------------------------------------------
            if (list_of_ex_values[15] == True):
                if (list_of_ex_values[21] == False):
                    conditions = row["conditions"]
                    if "Overcast" in conditions:
                        value = 100
                    elif "Partially cloudy" in conditions or "Clear" in conditions:
                        value = 0
                        br_row_unpopulated["cloudcover"] = 0
                        for k in range(len(df.index) - i - 1):
                            if pd.isnull(df.iloc[i + k + 1, 15]) == False:
                                value = round((past_values["cloudcover"] + df.iloc[i + k + 1, 15]) / 2, 1)
                                break
                            else:
                                br_row_unpopulated["cloudcover"] += 1
                        if "Partially cloudy" in conditions:
                            if value < 20:
                                value = 20
                            elif value > 99:
                                value = 99
                        elif "Clear" in conditions:
                            if value >= 20:
                                value = 19
                    else:
                        value = 0
                    df.iloc[i, 15] = value
                    row["cloudcover"] = value
                    past_values["cloudcover"] = value
                    if br_row_unpopulated["cloudcover"] > 0:
                        br_row_unpopulated["cloudcover"] -= 1
                else:
                    if br_row_unpopulated["cloudcover"] > 0:
                        df.iloc[i, 15] = past_values["cloudcover"]
                        row["cloudcover"] = past_values["cloudcover"]
                        br_row_unpopulated["cloudcover"] -= 1
                    else:
                        br_row_unpopulated["cloudcover"] = 0
                        for k in range(len(df.index) - i - 1):
                            if pd.isnull(df.iloc[i + k + 1, 15]) == False:
                                value = round((past_values["cloudcover"] + df.iloc[i + k + 1, 15]) / 2, 1)
                                past_values["cloudcover"] = value
                                df.iloc[i, 15] = value
                                row["cloudcover"] = value
                                break
                            else:
                                br_row_unpopulated["cloudcover"] += 1
            else:
                past_values["cloudcover"] = row["cloudcover"]

            #---------------------CONDITION-------------------------------------------
            if (list_of_ex_values[21] == True):
                conditions = ""
                if row["precip"] > 0:
                    if "Snow" in past_values["conditions"]:
                        conditions = "Snow, "
                    else:
                        conditions = "Rain, "
                if row["cloudcover"] == 100:
                    conditions += "Overcast"
                elif row["cloudcover"] >= 20 and row["cloudcover"] <= 99:
                    conditions += "Partially cloudy"
                else:
                    conditions += "Clear"
                past_values["conditions"] = conditions
                df.iloc[i, 21] = conditions
                row["cloudcover"] = conditions
            else:
                past_values["conditions"] = row["conditions"]

            # print(df["feelslike"].isna().sum())
        return df

    def calculateWindspeedFromFeelslike(self, temp, feelslike):
        a = (feelslike - 35.74 - 0.6215 * temp) / (0.4275 * temp - 35.75)
        if a < 0:
            return -1
        windspeed = round(math.pow(a, 1 / 0.16), 1)
        return windspeed

    def calculateFeelslike(self, temp, windspeed=None, humidity=None):
        feelslike = temp
        if temp <= 50:
            feelslike = round(35.74 + (0.6215 * temp) - (35.75 * math.pow(windspeed, 0.16)) + (0.4275 * temp * math.pow(windspeed, 0.16)), 1)
        elif temp >= 80:
            feelslike = round(-42.379 + (2.04901523 * temp) + (10.14333127 * humidity) \
                              - (0.22475541 * temp * humidity) - (6.83783 * math.pow(10, -3) * math.pow(temp, 2)) \
                              - (5.481717 * math.pow(10, -2) * math.pow(humidity, 2)) + (1.22874 * math.pow(10, -3) * math.pow(temp, 2) * humidity) \
                              + (8.5282 * math.pow(10, -4) * temp * math.pow(humidity, 2)) - (1.99 * math.pow(10, -6) * math.pow(temp, 2) * math.pow(humidity, 2)), 1)
        return feelslike

    def calculateDew(self, temp, humidity):
        temp_in_c = self.fromFtoC(temp)
        dew = (243.04 * (math.log(humidity / 100) + 17.625 * temp_in_c / (243.04 + temp_in_c))) / (
                    17.625 - (math.log(humidity / 100) + 17.625 * temp_in_c / (243.04 + temp_in_c)))
        return round(self.fromCtoF(dew), 1)

    def calculateHumidity(self, temp, dew):
        dew_in_c = self.fromFtoC(dew)
        temp_in_c = self.fromFtoC(temp)
        humidity = 100 * (math.pow(math.e, 17.625 * dew_in_c / (243.04 + dew_in_c)) / math.pow(math.e, 7.625 * temp_in_c / (243.04 + temp_in_c)))
        return round(humidity, 2)

    def fromFtoC(self, x):
        return (x - 32) / 1.8

    def fromCtoF(self, x):
        return 1.8 * x + 32

    def closeRepository(self):
        self.datasetRepository.closeConnection()

    def loadHolidays(self):
        holidays = {
            "2018": [datetime.datetime(2018, 1, 1), datetime.datetime(2018, 1, 15), datetime.datetime(2018, 2, 14),
                     datetime.datetime(2018, 2, 19), datetime.datetime(2018, 3, 30), datetime.datetime(2018, 4, 1),
                     datetime.datetime(2018, 5, 13), datetime.datetime(2018, 5, 28), datetime.datetime(2018, 6, 1),
                     datetime.datetime(2018, 6, 17), datetime.datetime(2018, 7, 4), datetime.datetime(2018, 9, 3),
                     datetime.datetime(2018, 10, 8), datetime.datetime(2018, 10, 31), datetime.datetime(2018, 11, 11),
                     datetime.datetime(2018, 11, 22), datetime.datetime(2018, 12, 25)],
            "2019": [datetime.datetime(2019, 1, 1), datetime.datetime(2019, 1, 21), datetime.datetime(2019, 2, 14),
                     datetime.datetime(2019, 2, 18), datetime.datetime(2019, 4, 19), datetime.datetime(2019, 4, 21),
                     datetime.datetime(2019, 5, 12), datetime.datetime(2019, 5, 27), datetime.datetime(2019, 6, 16),
                     datetime.datetime(2019, 7, 4), datetime.datetime(2019, 9, 2), datetime.datetime(2019, 10, 14),
                     datetime.datetime(2019, 10, 31), datetime.datetime(2019, 11, 11), datetime.datetime(2019, 11, 28),
                     datetime.datetime(2019, 12, 25)],
            "2020": [datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 20), datetime.datetime(2020, 2, 14),
                     datetime.datetime(2020, 2, 17), datetime.datetime(2020, 4, 10), datetime.datetime(2020, 4, 12),
                     datetime.datetime(2020, 5, 10), datetime.datetime(2020, 5, 25), datetime.datetime(2020, 6, 21),
                     datetime.datetime(2020, 7, 3), datetime.datetime(2020, 7, 4), datetime.datetime(2020, 9, 7),
                     datetime.datetime(2020, 10, 12), datetime.datetime(2020, 10, 31), datetime.datetime(2020, 11, 11),
                     datetime.datetime(2020, 11, 26), datetime.datetime(2020, 12, 25)],
            "2021": [datetime.datetime(2021, 1, 1), datetime.datetime(2020, 1, 18), datetime.datetime(2020, 2, 14),
                     datetime.datetime(2020, 2, 15), datetime.datetime(2020, 4, 2), datetime.datetime(2020, 4, 4),
                     datetime.datetime(2020, 5, 9), datetime.datetime(2020, 5, 31), datetime.datetime(2020, 6, 20),
                     datetime.datetime(2020, 7, 4), datetime.datetime(2020, 9, 6), datetime.datetime(2020, 10, 11),
                     datetime.datetime(2020, 10, 31), datetime.datetime(2020, 11, 11), datetime.datetime(2020, 11, 25),
                     datetime.datetime(2020, 12, 25)]
        }
        return holidays

