from app import app, db
from flask import render_template, url_for, request, redirect, Response
from app.models import Shop
import uuid
from datetime import time


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        return render_template('index.jinja2', times=int(data['times']), text=data['text'])
    return render_template('index.jinja2')


@app.route('/add_shop', methods=['POST'])
def add_shop():
    data = request.get_json()
    for i in range(int(data['times'])):
        shop = Shop(name=str(uuid.uuid4()), city=str(uuid.uuid4()), street=str(uuid.uuid4(
                )), street_number=7, open_at=time(hour=7, minute=0), close_at=time(hour=21, minute=0))
        db.session.add(shop)
        db.session.commit()
    return Response(status=201)
    

@app.route('/clear_shops_table', methods=['POST'])
def clear_shops_table():
    db.session.query(Shop).delete()
    return Response(status=200)
