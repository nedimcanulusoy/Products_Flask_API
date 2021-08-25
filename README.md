<h3 align="center">
    This is a simple REST API project written in Python, Flask
</h3>

| Request                                    | Type   | Feature                                                             | Method                  |
|--------------------------------------------|--------|---------------------------------------------------------------------|-------------------------|
| http://localhost:5000/store/api/products   | GET    | @app.route('/store/api/products', methods=['GET'])                  | get_products()          |
| http://localhost:5000/store/api/products/1 | GET    | @app.route('/store/api/products/\<int:prod_id>', methods=['GET'])    | get_product(prod_id)    |
| http://localhost:5000/store/api/products   | POST   | @app.route('/store/api/products', methods=['POST'])                 | create_product()        |
| http://localhost:5000/store/api/products/2 | DELETE | @app.route('/store/api/products/\<int:prod_id>', methods=['DELETE']) | delete_product(prod_id) |
