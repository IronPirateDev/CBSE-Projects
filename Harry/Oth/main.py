from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/scan_qr', methods=['POST'])
def scan_qr():
  code = request.form['code']
  # Process the scanned QR code (e.g., print it)
  print("Scanned QR Code:", code)
  return render_template('hi.html')


if __name__ == '__main__':
  app.run(debug=True, port=5000, host='0.0.0.0')
