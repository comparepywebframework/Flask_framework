from app import app, db
from flask import render_template, url_for, request, redirect, Response, jsonify
from app.models import Shop, Student
import uuid
from datetime import time, date
import requests
import json


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
    db.session.commit()
    return Response(status=200)


@app.route('/external_api_call')
def external_api_call():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=3096472&APPID=39d3a15f5bdcab980c739b931b9c2863')
    return Response(r.text)


@app.route('/serialize_json')
def serialize_json():
    id_number = str(uuid.uuid4())
    student = Student(name="Jim", surname="Bim", date_of_birth=date(1990, 1, 1), id_number=id_number)
    db.session.add(student)
    db.session.commit()
    student = db.session.query(Student).filter_by(id_number=id_number).first()
    return jsonify({"name": student.name, "surname": student.surname, "date_of_birth": student.date_of_birth, "id_number": student.id_number})


@app.route('/clear_students_table')
def clean_students_table():
    db.session.query(Student).delete()
    db.session.commit()
    return Response(status=200)