from fastapi import FastAPI
from enum import Enum

app = FastAPI()

#Get Request
@app.get("/hello/{name}")
def hello(name):
    return f'Welcome {name}!'


food_items = {

    'indian' : ['Samosa', 'Tikka'],
    'american' : ['Hot Dog', 'Apple Pie'],
    'italian' : ['Ravioli', 'Pizza']
}

class AvailableCuisines(str, Enum):

    indian = 'indian',
    american = 'american',
    italian = 'italian'

@app.get('/get_items/{cuisine}')
def get_items(cuisine : AvailableCuisines):
    return food_items.get(cuisine)


coupon_code = {

    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get('/get_coupon/{coupon}')
def get_coupon(coupon : int):
    return {'Discount' : coupon_code.get(coupon)}


#Post Request
#@app.api_route('/postData', methods=['GET','POST'])
@app.post('/postData')
def post_data(username : str):
    return {
        'username' : username
    }