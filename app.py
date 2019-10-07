
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give'] #클라이언트로부터 Name을 받는 부분
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    item_receive = request.form['item_give']



    orders = {'name': name_receive, 'count': count_receive, 'address': address_receive, 'phone': phone_receive, 'item': item_receive}


    db.orders.insert_one(orders)

    return jsonify({'result': 'success'})

@app.route('/order', methods=['GET'])
def listing():
    item_receive = request.args.get('item_give')

    result = list(db.orders.find({'item':item_receive},{'_id':0}))

    return jsonify({'result':'success', 'orders':result})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
