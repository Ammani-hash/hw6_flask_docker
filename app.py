from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
#from models import db, Item
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import SQLAlchemyError
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'

db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # local DB
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Get all rows
    return jsonify([item.to_dict() for item in items]), 200, {'Content-Type': 'application/json'}

@app.route('/api/items', methods=['POST'])
def create_item():
    try:
        data = request.get_json()  # Get JSON payload
        name = data.get('name')   # Extract the 'name'

        if not name:
            return jsonify({"error": "Missing 'name' field"}), 400

        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({"message": "Item inserted successfully"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
