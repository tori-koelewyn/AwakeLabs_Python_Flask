from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configuration settings
# Change for your Datebase User:
app.config['MYSQL_DATABASE_USER'] = 'root'
# Change for your Database Password:
app.config['MYSQL_DATABASE_PASSWORD'] = 'HDCycle2010'
app.config['MYSQL_DATABASE_DB'] = 'awake_labs_hike'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('awake_labs_main_page.html')

@app.route('/showCreate')
def showCreate():
    return render_template('create.html')

@app.route('/showUpdate')
def showUpdate():
    return render_template('update.html')

@app.route('/showDelete')
def showDelete():
    return render_template('delete.html')

@app.route('/createEntry',methods=['POST','GET'])
def createEntry():
    try:
        # puts the inputs into variables name, location, and image
        _name = request.form['inputHikeName']
        _location = request.form['inputHikeLocation']
        _duration = request.form['inputHikeDuration']

        # ensure the received values are valid
        if _name and _location and _duration:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser', (_name, _location, _duration))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'Hike Entry created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Please re-enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()
