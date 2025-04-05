from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

cars = []
next_id = 1

@app.route('/')
def home():
    return render_template('home.html', cars=cars)

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/cars', methods=['POST'])
def add_car():
    global next_id
    name = request.json.get('name')
    if not name:
        return jsonify({"error": "Missing car name"}), 400
    car = {"id": next_id, "name": name}
    cars.append(car)
    next_id += 1
    return jsonify(car), 201

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    global cars
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        return jsonify({"error": "Car not found"}), 404
    cars = [car for car in cars if car["id"] != car_id]
    return jsonify({"message": "Car deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
