from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/codec', methods=['POST'])
def encode():
    print(request.data)
    return 'w'

if __name__ == '__main__':
    app.run()