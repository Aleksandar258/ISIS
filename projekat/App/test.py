import math

# def f(dew, temp):
#     dew_in_c = fromFtoC(dew)
#     temp_in_c = fromFtoC(temp)
#     humidity = 100 * (math.pow(math.e, 17.625 * dew_in_c / (243.04 + dew_in_c)) / math.pow(math.e, 17.625 * temp_in_c / (243.04 + temp_in_c)))
#     return round(humidity, 2)
#
#
def fromFtoC(x):
    return (x-32) / 1.8
#
#
# print(f(-3.5, 9.2))


# def f(temp, windspeed, humidity):
#     feelslike = temp
#     if temp <= 50:
#         feelslike = round(35.74 + (0.6215 * temp) - (35.75 * math.pow(windspeed, 0.16)) + (0.4275 * temp * math.pow(windspeed, 0.16)), 1)
#     elif temp >= 80:
#         feelslike = round(-42.379 + (2.04901523 * temp) + (10.14333127 * humidity) \
#                     - (0.22475541 * temp * humidity) - (6.83783 * math.pow(10, -3) * math.pow(temp, 2)) \
#                     - (5.481717 * math.pow(10, -2) * math.pow(humidity, 2)) + (1.22874 * math.pow(10, -3) * math.pow(temp, 2) * humidity) \
#                     + (8.5282 * math.pow(10, -4) * temp * math.pow(humidity, 2)) - (1.99 * math.pow(10, -6) * math.pow(temp, 2) * math.pow(humidity, 2)), 1)
#
#     return feelslike
#
#
# print(f(83.9, 11.3, 32.44))

# def f(temp, feelslike):
#     a = -1.99 * math.pow(10, -3) * math.pow(temp, 2) + 8.5282 * math.pow(10, -4) * temp - 5.481717 * math.pow(10, 2)
#     b = 10.14333127 - 0.22475541 * temp + 1.22874 * math.pow(10, -3) * math.pow(temp, 2)
#     print(a, b)
#     humidity = (math.sqrt(feelslike + math.pow(b, 2) / 4 * a) - b / 2 * math.sqrt(a)) / math.sqrt(a)
#     return humidity
#
#
# print(f(83.9, 82.2))

def fromCtoF(x):
    return 1.8 * x + 32
#
# def f(temp, humidity):
#     temp_in_c = fromFtoC(temp)
#     dew = (243.04 * (math.log(humidity/100) + 17.625 * temp_in_c / (243.04 + temp_in_c))) / (17.625 - (math.log(humidity / 100) + 17.625 * temp_in_c / (243.04 + temp_in_c)))
#     return round(fromCtoF(dew), 1)


# print(f(9.2, 55.55))

# def f(temp, feelslike):
#     a = (feelslike - 35.74 - 0.6215 * temp) / (0.4275 * temp - 35.75)
#     windspeed = round(math.pow(a, 1/0.16), 1)
#     return windspeed
#
# print(f(7.5, -6.4))

# def f(d, m, y1, y2):
#     if m < 3:
#         m += 10
#         y -= 1
#     else:
#         m -= 2
#     re = d + math.floor((13 * m - 1) / 5) + y2 + math.floor(y2 / 4) + math.floor(y1 / 4) - 2 * y1
#     print(re)
#     rez = int(re)
#     print(rez)
#     return rez%7
#
# print(f(2, 3, 20, 4))

print(2021%100)


