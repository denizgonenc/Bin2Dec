from flask import Flask, request, render_template, jsonify
from bin2dec import bin2dec

app = Flask(__name__, static_url_path='/static')

@app.route('/bin2dec', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        binary = request.form['binary']
        decimal = bin2dec(binary)
        print(decimal)
        return jsonify(dec=decimal)
    else:
        return render_template('bin2dec.html')



if __name__ == '__main__':
    app.run()