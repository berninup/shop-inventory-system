from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute('''
        SELECT Items.*, Totes.ToteDescription, Locations.LocationDescription 
        FROM Items 
        JOIN Totes ON Items.ToteID = Totes.ToteID 
        JOIN Locations ON Totes.LocationID = Locations.LocationID 
        WHERE ItemID = ?''', (item_id,)).fetchone()
    conn.close()

    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    item_dict = {
        'ItemID': item['ItemID'],
        'ItemName': item['ItemName'],
        'Description': item['Description'],
        'Keywords': item['Keywords'],
        'ToteDescription': item['ToteDescription'],
        'LocationDescription': item['LocationDescription']
    }
    return jsonify(item_dict)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
