from flask import Flask, render_template, request, jsonify, redirect
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/setdb')
def setdb():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute(
            'CREATE TABLE entries (id INTEGER NOT NULL PRIMARY KEY,date TEXT, name TEXT, content TEXT)')
        con.commit()
    return '"Table created successfully"'


@app.route('/create', methods=['POST'])
def create():
    print(request.json['date'])

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO entries (date,name,content) values (?,?,?)",
                    (
                        request.json['date'],
                        request.json['firstname'],
                        request.json['content']
                    )
                    )
        con.commit()
        print("Record successfully added")

    return 'ok'


@app.route('/list', methods=['GET'])
def list():

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * from entries;")
        rows = cur.fetchall()

    print(rows)

    return jsonify(rows)


@app.route('/delete/<int:eid>', methods=['GET'])
def delete(eid):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        print(type(eid))
        cur.execute("DELETE FROM entries WHERE id = ?;", (eid,))
        con.commit()
        print("Record successfully deleted")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
