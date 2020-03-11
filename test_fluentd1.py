#from flask import Flask, render_template, jsonify, request
from datetime import datetime
#import joblib
#import pandas as pd
#import decision_tree
#import os
from fluent import sender#, event

#TENANT = os.getenv('TENANT', 'local')
FLUENTD_HOST = 'localhost' #os.getenv('FLUENTD_HOST')
FLUENTD_PORT = 24224 #8888 #os.getenv('FLUENTD_PORT')

products = {
    "99197": {
        "class": 1067,
        "family": "GROCERY I",
        "perishable": 0
    },
    "105574": {
        "class": 1045,
        "family": "GROCERY I",
        "perishable": 0
    },
    "1963838": {
        "class": 3024,
        "family": "CLEANING",
        "perishable": 0
    }
}


import random, time

#get a random item number
item_nbr = random.choice(list(products.keys()))
product = products[str(item_nbr)]

#get a random date
def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

date_string = random_date("1/1/2000 1:30 PM", "1/1/2020 4:50 AM", random.random()) #request.args.get('date')

date = datetime.strptime(date_string,'%m/%d/%Y %H:%M %p')

data = {
    "date": date_string,
    "item_nbr": item_nbr, #request.args.get("item_nbr"),
    "family": product['family'],
    "class": product['class'],
    "perishable": product['perishable'],
    "transactions": 1000,
    "year": date.year,
    "month": date.month,
    "day": date.day,
    "dayofweek": date.weekday(),
    "days_til_end_of_data": 0,
    "dayoff": date.weekday() >= 5
}
#print('TENANT is ', TENANT)
  
logger = sender.FluentSender('local', host=FLUENTD_HOST, port=int(FLUENTD_PORT))
#logger = sender.setup('local', host=FLUENTD_HOST, port=int(FLUENTD_PORT))
log_payload = {'prediction': random.randint(1,100), **data}
print('logging {}'.format(log_payload))
if not logger.emit('prediction', log_payload):
    print('..in if not..')
    print(logger.last_error)
    logger.clear_last_error()

