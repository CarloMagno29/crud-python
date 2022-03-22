from flask import jsonify
import json

yeison = "mock.json"


def reader_json():
    try:
       with open(yeison, "r") as leer:
           data = json.load(leer)            
           return data
    except:
        return None
    finally:    
        leer.close()


def writer_json(data):
    with open(yeison, "w") as escribir:
        try:
            escribir.write(json.dumps(data))
        except:
            return jsonify("write read file")    
        finally:
            escribir.close()        