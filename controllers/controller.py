from app import app
from flask import render_template
from models.order_list import *

@app.route('/orders')
def index():
        return render_template('index.html', Title="Orders Website", Heading = "All Orders", orders = orders)

@app.route('/orders/<index>')
def order(index):
    order = orders[int(index)]
    return render_template('order.html', Title="Order", order = order)
