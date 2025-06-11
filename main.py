from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/<Property_ID>', methods=['GET'])
def get_property(Property_ID):
    # Simulated database of properties
    properties = {
        "1": {"name": "Cliffs Mansion", "location": "Coorg","Owner_ID": "12345", "price": 100000, "rent":10000},
        "2": {"name": "Ocean View Villa", "location": "Goa", "Owner_ID": "67890", "price": 200000, "rent": 20000},
        "3": {"name": "Mountain Retreat", "location": "Himachal", "Owner_ID": "54321", "price": 300000, "rent": 0}
    }
    
    property_data = properties.get(Property_ID)
    
    if property_data:
        return jsonify(property_data), 200
    else:
        return jsonify({"error": "Property not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
