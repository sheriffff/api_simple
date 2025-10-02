from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola colegui"


@app.route('/multiply', methods=['POST'])
def create_item():
    if not request.json or 'number' not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    number = request.json['number']
    number_times_two = number * 2

    return jsonify({"doubled": number_times_two}, 200)


if __name__ == '__main__':
    app.run(debug=True)