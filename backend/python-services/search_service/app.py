from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration
vehicles = {
    'cars': [
        {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020},
        {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2021}
    ],
    'buses': [
        {'id': 1, 'company': 'Greyhound', 'route': 'New York to Boston'},
        {'id': 2, 'company': 'Megabus', 'route': 'Los Angeles to San Francisco'}
    ],
    'trains': [
        {'id': 1, 'company': 'Amtrak', 'route': 'Chicago to New York'},
        {'id': 2, 'company': 'Eurostar', 'route': 'London to Paris'}
    ]
}

@app.route('/search', methods=['GET'])
def search():
    vehicle_type = request.args.get('type')
    if vehicle_type in vehicles:
        return jsonify(vehicles[vehicle_type]), 200
    return jsonify({'error': 'Vehicle type not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)