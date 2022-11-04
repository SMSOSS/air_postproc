from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
import pandas as pd
import datetime
import logging
import random 
import csv

from sklearn.linear_model import LinearRegression
import joblib
from os import path , remove
import warnings

from weather import check_weather
from date import check_date

volume = 0
count = 0

logging.basicConfig(level = logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('sensor.log','w' , 'utf-8'),])

def collect_data():
    print("D")
    with open('sensor.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([int(datetime.datetime.utcnow().timestamp()) , count , volume])
    logging.debug(f"Data added : {count} {volume}%")
    
    with open('data.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        holiday = check_date(datetime.date.today().year , datetime.date.today().month , datetime.date.today().day)[0]
        weekend = check_date(datetime.date.today().year , datetime.date.today().month , datetime.date.today().day)[1]
        writer.writerow([check_weather()  , holiday , weekend,  int(datetime.datetime.utcnow().timestamp()) , count , volume])

def build_model():
    df2 = pd.read_csv("data.csv")
    X = df2.drop(columns=['volume'])
    y = df2['volume']

    lr = LinearRegression()
    lr.fit(X, y)

    if path.exists("bin_data_model.joblib"):
        remove("bin_data_model.joblib")

    joblib.dump(lr, "bin_data_model")

    logging.debug(f"Model updated")

def predict(weather , holiday , weekend , rubbish_count):
    if not path.exists("bin_data_model.joblib"):
        warnings.warn("Warning : model not found!")
    else:
        model = joblib("bin_data_model.joblib")
        result = model.predict([weather , holiday , weekend , rubbish_count])
        return result

#collect_data()
scheduler = BackgroundScheduler(timezone='Asia/Hong_Kong')
scheduler.add_job(collect_data, 'interval', seconds=10)
scheduler.start()

while True:
    # sensor get data
    sleep(5)
    volume += random.randint(1,10)
    count += random.randint(1,5)
