from flask import Flask, jsonify
import FoodWebscrape
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<string:restrictions>")
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_food(restrictions):
    return jsonify(FoodWebscrape.get_food(restrictions))

if __name__ == "__main__":
    app.run()