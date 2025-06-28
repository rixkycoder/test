from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test_endpoint():
    data = request.get_json()
    message = data.get('message', 'No message received')
    response = {'reply': f'Server received: {message}'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
