from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from flask import make_response
import os

app = Flask(__name__)

menu_items = [
	{
		'name':'Chicken Tikka Masala',
		'restaurant':'Madras Chettinaad',
		'location':'Alpharetta, GA',
		'price':'12',
		'description':'A savory blend of spices mixed with lentils and poured delicately on top of chicken breast',
		'ingredients':'Chicken, yogurt, cream, tomato, onion, garlic, ginger, chili pepper, coconut'
	}
]

@app.route('/home', methods=['GET'])
def main_page():
	return 'GET /getItems: list of items with details \n POST /postDataForItem: name, restaurant, location, price, description, ingredients'

@app.route('/', methods=['GET'])
def init_page():
	return 'iEatOut API. See repo for details'

@app.route('/getItems', methods=['GET'])
def get_items():
	return jsonify({'menu_items':menu_items})

@app.route('/postDataForItem', methods=['POST'])
def post_item():
	if not request.json:
		abort(400)
	item = {
		'name':request.json['name'],
		'restaurant':request.json['restaurant'],
		'location':request.json['location'],
		'price':request.json['price'],
		'description':request.json['description'],
		'ingredients':request.json['ingredients']
	}
	menu_items.append(item)
	return jsonify({'new_item':item}), 201

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)


