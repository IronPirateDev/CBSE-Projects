# app.py

from flask import Flask, render_template, request, jsonify
import cv2
from pyzbar.pyzbar import decode
import mysql.connector as c

app = Flask(__name__)

# Database connection
con = c.connect(user='root', passwd='dpsbn', host='localhost', database='ticket')
cu = con.cursor()

# Function to decode QR code
def decode_qr(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        return barcodeData, barcodeType

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr')
def qrscan():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoded_data = decode_qr(frame)
        if decoded_data:
            break
        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    # Pass the decoded data to the template
    return render_template('qr.html', code=decoded_data[0])

@app.route('/add_guest', methods=['GET', 'POST'])
def add_guest():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']

        # Add your logic to insert guest into the database
        query = "INSERT INTO guest(name, code) VALUES (%s, %s)"
        cu.execute(query, (name, code))
        con.commit()

        return jsonify({'message': 'Guest added successfully'})

    return render_template('add_guest.html')

@app.route('/rowcount')
def rowcount():
    # Count the number of rows in the guest table
    query = "SELECT COUNT(*) FROM guest"
    cu.execute(query)
    count = cu.fetchone()[0]

    return render_template('rowcount.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)
