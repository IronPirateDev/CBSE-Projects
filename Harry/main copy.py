from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/qr')
def qrscan():
    return render_template('qr.html')
@app.route('/process_option', methods=['POST'])
def process_option():
    data = request.get_json()
    option = data['option']
    return jsonify({'message': 'Option processed successfully'})
if __name__ == '__main__':
    app.run(debug=True)