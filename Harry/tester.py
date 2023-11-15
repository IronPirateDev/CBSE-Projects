from flask import Flask, request, render_template
import mysql.connector as ms
db = ms.connect(host='localhost', user='root', password='dpsbn', database='ticket')
app = Flask(__name__)
cursor = db.cursor()
def presence(no):
    cursor.execute('select entry from guest where code like %s', (no,))
    s = cursor.fetchall()
    s = s[0][0]
    return s
@app.route('/')
def index():
    #welcome_message = "Welcome to the QR Code Scanner!"
    return render_template('index.html')
@app.route('/qr')
def qr():
    #welcome_message = "Welcome to the QR Code Scanner!"
    return render_template('qr.html')
@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    scanned_data = data.get('data', '')
    print('Scanned QR Code on the server:', scanned_data)
    res=presence(scanned_data)
    prff=''
    if res == 'False':
        cursor.execute('update guest set entry = \'True\' where code = %s',(scanned_data,))
        db.commit()
        prff='Welcome TO Grad 24'
    else:
        prff='Entry Declined'
    return prff
@app.route('/total_entries')
def total_entries():
    cursor.execute('select count(*) from guest')
    z = cursor.fetchone()[0]
    return render_template('total_entries.html', z=z)
if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
db.close()