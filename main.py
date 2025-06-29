from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/<Property_ID>', methods=['GET'])
def get_property(Property_ID):
    # Simulated database of properties
    properties = {
        "1": {"name": "Cliffs Mansion", "location": "Coorg","Owner_ID": "12345", "price": 100000, "rent":1000000000000000},
        "2": {"name": "Ocean View Villa", "location": "Goa", "Owner_ID": "67890", "price": 200000, "rent": 2000000000000000},
        "3": {"name": "Mountain Retreat", "location": "Himachal", "Owner_ID": "54321", "price": 300000, "rent": 0},
        "4": {"name": "Mountain Retreat", "location": "Himachal", "Owner_ID": "54321", "price": 300000, "rent": 15000},
        "5": {"name": "Coastal Haven", "location": "Goa", "Owner_ID": "98765", "price": 7500000, "rent": 35000},
        "6": {"name": "City View Apartment", "location": "Mumbai", "Owner_ID": "11223", "price": 12000000, "rent": 60000},
        "7": {"name": "Desert Oasis Villa", "location": "Rajasthan", "Owner_ID": "44556", "price": 9000000, "rent": 40000},
        "8": {"name": "Riverside Cabin", "location": "Kerala", "Owner_ID": "77889", "price": 4500000, "rent": 22000},
        "9": {"name": "Urban Loft", "location": "Bangalore", "Owner_ID": "22334", "price": 10000000000000000000, "rent": 15000000000000000},
        "10": {"name": "Forest Bungalow", "location": "Uttarakhand", "Owner_ID": "66778", "price": 27500000000000000000, "rent": 20000000000000000},
        "11": {"name": "Lakefront Cottage", "location": "Srinagar", "Owner_ID": "33445", "price": 17863546200000000000, "rent": 20000000000000000},
        "12": {"name": "Country Farmhouse", "location": "Punjab", "Owner_ID": "99001", "price": 10230000000000000000, "rent": 10230000000000000},
        "13": {"name": "Beach House", "location": "Puducherry", "Owner_ID": "10112", "price": 1870000000000000000, "rent": 20000000000000000}
    }
    
    property_data = properties.get(Property_ID)
    
    if property_data:
        return jsonify(property_data), 200
    else:
        return jsonify({"error": "Property not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
