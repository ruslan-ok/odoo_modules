import pandas as pd
import json

with open('points.json') as data_file:
    data = json.load(data_file)
df = pd.json_normalize(data, 'items')
# n - id
# t - ? {1, 2}
# d - description
# m - maybe parent id
# q - ? {'', 33, 30}
# f - ? {'', '002', '008', '006', '003', '004', '005', '001', '007'}
# c - city
# g - city in english
# e - street
# r - area
# o - zip
# b - building number
# h - work time weekly
# i - work time by days
# p - ? {0, 1}
# s - ? {1}
# l.a - latitude
# l.o - longitude
df_dbg = df[df['g'] == 'wroclaw'][['n', 'd', 'c', 'g', 'e', 'r', 'o', 'b', 'l.a', 'l.o']]
#df_dbg.to_csv('parcel.locker.csv', index=False, header=['code', 'description', 'city', 'city_eng', 'street', 'area', 'zip', 'building', 'latitude', 'longitude'])
df_dbg.to_csv('parcel.locker.csv', header=['code', 'description', 'city', 'city_eng', 'street', 'area', 'zip', 'building', 'latitude', 'longitude'])
