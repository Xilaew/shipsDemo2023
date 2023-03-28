from flask import Flask, jsonify, request

app = Flask(__name__)

# Definiere eine einfache Route
@app.route('/')
def hello():
    return "Hello World!"

# Definiere eine API Route, welche JSON zurückgibt
@app.route('/api')
def api():
    data = {"message": "Hello World!"}
    return jsonify(data)

# Erstelle ein zweidimensionales Feld für Text
text_feld = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# Route für das Setzen des Texts in das Feld
@app.route('/set_text', methods=['POST'])
def set_text():
    x = int(request.form['x'])
    y = int(request.form['y'])
    text = request.form['text']
    text_feld[x][y] = text
    return jsonify({'success': True})

# Route für das Abrufen des Texts aus dem Feld
@app.route('/get_text', methods=['GET'])
def get_text():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({'text': text_feld[x][y]})

if __name__ == '__main__':
    app.run(debug=True)
