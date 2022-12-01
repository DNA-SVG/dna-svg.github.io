from flask import Flask, render_template, url_for, request
import sys, os
sys.path.append(os.getcwd()+'\\codec\\codec')
import codec as cd
print(sys.path)

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/codec/<action>', methods=['POST'])
def codec(action=None):
    print(request.data)
    if action == 'encode':
        return cd.svg_to_dna(request.data.decode(encoding='utf-8'))
    else:
        return cd.dna_to_svg(request.data.decode(encoding='utf-8'))

if __name__ == '__main__':
    app.run()