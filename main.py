from fastapi import FastAPI
import json
#-*- coding: utf-8 -*-
app = FastAPI()

  
# @app.get('/bmi')
# x:int:xxx (if none value x = xxx)
def bmi(h : int = 170, w: int = 50):

    h   = (h/100) **2
    bmi = w/h

    return{'bmi': bmi}

@app.get('/riceall')
def riceall():
    data = json.load(open('data.json'))
    return {'data':data}

@app.get('/ricecalculator')
# w = weight, u = unit of weight
def cal_rice_price(type: str = 'tj', w: int = 10, u: str = 'kg'):
    data = json.load(open('data.json'))
    if u == 't':
        result = data[type]['price']*w
    else :
        result = (data[type]['price']/1000)*w
    return{
        'type'      :type,
        'name_eng'  :data[type]['nameeng'],
        'weight'    :w,
        'unit'      :u,
        'price'     : result
    }
# ::hx = the humidity appears ::hy = the humidity need
@app.get('/ricecalculator/humidity')
def rice_humidity(type: str = 'tj', humidity: int = 25, dehumidify: int = 15):
    data = json.load(open('data.json'))
    w    = 1
    if dehumidify > 15:
        w = 15*(dehumidify - 15)
    weight_humidity = (humidity - dehumidify)*w
    balance         = 1000 - weight_humidity
    result          = (data[type]['price'])/balance
    return{
        'type'      :type,
        'name_eng'  :data[type]['nameeng'],
        'weight'    :w,
        'humidity'  :humidity,
        'dehumidify':dehumidify,
        'totol'     :result,
        'unit'      :"bath/kg"
    }
    