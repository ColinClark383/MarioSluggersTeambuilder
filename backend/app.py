from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  #allow all domains to access

DATABASE = 'sluggers.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries for convenience
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)


@app.route('/api/roster', methods=['POST'])
def handle_roster():
    data = request.get_json()  

    conn = get_db_connection()
    cursor = conn.cursor()

    charecterList = [row[0].lower() for row in cursor.execute('''
        SELECT name FROM Sluggers WHERE varients = 1;
    ''').fetchall()]
    varientList = [row[0].lower() for row in cursor.execute('''
        SELECT varient FROM Varients;
    ''').fetchall()]

    taken_chars = []
    bad_slots = []
    i = 0
    for player in data.get('player1team'):
        if player.lower() not in charecterList and player.lower() not in varientList:
            bad_slots.append(i)
        elif player.lower() in taken_chars and player.lower() != 'mii':
            bad_slots.append(i)
        else:
            taken_chars.append(player.lower())
        i += 1

    for player in data.get('player2team'):
        if player.lower() not in charecterList and player.lower() not in varientList:
            bad_slots.append(i)
        elif player.lower() in taken_chars and player.lower() != 'mii':
            bad_slots.append(i)
        else:
            taken_chars.append(player.lower())
        i += 1

    conn.close()

    print(bad_slots)

    return jsonify({'message': 'Roster received successfully!', 'data': bad_slots})

if __name__ == '__main__':
    app.run(debug=True)

