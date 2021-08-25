from products_api import app
from flask import Flask, jsonify, make_response, request

products = [
    {
        'id': 1,
        'title': 'Pen Set',
        'description': 'This Pen set has 16 different colours.',
        'price': 50,
        'category':'School',
        'inStock':True
    },
    {
        'id': 2,
        'title': 'Python Programming',
        'description': 'Introduction to Python',
        'price': 60,
        'category':'Book',
        'inStock':False
    },
    {
        'id': 3,
        'title': 'Ipad Mini',
        'description': 'Brand New 128 GB Ipad Mini',
        'price': 200,
        'category':'Electronic',
        'inStock':True
    },
    {
        'id': 4,
        'title': 'Ipad Mini',
        'description': 'Brand New 128 GB Ipad Mini',
        'price': 200,
        'category':'Electronic',
        'inStock':True
    }
]

@app.route('/store/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

@app.route('/store/api/products/<int:prod_id>', methods=['GET'])
def get_product(prod_id):
    for product in products:
        if product['id'] == prod_id:
            if len(product) == 0:
                return jsonify({'product': 'This product could not found!'}), 404
            return jsonify({'product': product})

@app.route('/store/api/products', methods=['POST'])
def create_product():
    new_product = {
        'id': products[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'price':request.json.get('price', 1),
        'category':request.json['category'],
        'inStock': request.json.get('inStock', False)
    }

    products.append(new_product)
    return jsonify({'product':new_product}), 201

@app.route('/store/api/products/<int:prod_id>', methods=['DELETE'])
def delete_product(prod_id):
    for product in products:
        if product['id'] == prod_id:
            if len(product) == 0:
                return jsonify({'product': 'This product could not found!'}), 404
            products.remove(product[0])
            return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'HTTP 404 Error': 'The content you are looking for does not exist. Please check your request.'}), 404)
