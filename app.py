from csv import reader
from itertools import product
from flask import Flask, jsonify, request
from flask_cors import CORS
from utilidades import writer_json, reader_json
import json

app = Flask(__name__)
CORS(app)

yeison = "mock.json"

@app.route("/reader", methods =["GET"])
def reader_users():
    try:
         with open(yeison, "r") as leer:
            data= json.load(leer)
            return data
    except:
        return None
    finally:    
        leer.close()

@app.route("/creator", methods =["POST"])
def create_user():
    detalle = request.args["detalle"]
    nombre = request.args["nombre"]
    stock = request.args["stock"]
    
    productos = {
            "detalle":detalle,
            "nombre":nombre,
            "stock":stock
         }       

    data = reader_json()
    data["productos"].append(productos)
    writer_json(data)
    
    return jsonify(data)


@app.route("/find", methods=["GET"])
def find_product():
     if request.method == "GET":
       nombre = request.args["nombre"] 
       data = reader_json()        

       for n in data["productos"]:
           if n["nombre"] == nombre:
            return jsonify(n) 


@app.route("/wipe", methods = ["DELETE"])
def delete_preduct():
         detalle = request.args["detalle"] 
         data = reader_json()        
       
         for idx, n in enumerate(data["productos"]):
            if n["detalle"] == detalle:
               data["detallle"].pop(idx) 
       
         writer_json(data)        
         return jsonify("erased") 


@app.route("/update", methods =["PUT"])
def update_product():
     if request.method == "PUT":
        d = request.args["nombre"]
        data = reader_json()


     for idx, n in enumerate(data["productos"]):
         if n["nombre"] == d:
             
            writer_json(data)        
         
         return jsonify("updated".format(n)) 
app.run(host="127.0.0.1", port=5000, debug=True)