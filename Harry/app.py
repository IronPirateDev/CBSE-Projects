import cv2
from flask import Flask, render_template

app = Flask(__name__)

def decode_qr(frame):
    import cv2
    from pyzbar.pyzbar import decode
    import numpy as np
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        return barcodeData, barcodeType

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan():
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

    code1 = None
    for i in decoded_data:
        code1 = i
        break

    return f"<h1>Scanned QR Code: {code1}</h1>"

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')