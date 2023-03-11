from flask import Flask, render_template, url_for, request
import codec.codec.codec as cd
import sys
sys.path.append("codec/simple-codec")
import simple

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/codec/<action>', methods=['POST'])
def do_codec(action=None):
    try:
        if len(request.data):
            if action == 'encode':
                return cd.svg_to_dna(request.data.decode(encoding='utf-8'))
            elif action == 'decode':
                return cd.dna_to_svg(request.data.decode(encoding='utf-8'))
            elif action == 'simple':
                seq = simple.encode(request.data)
                seq = "\n".join(simple.split(seq, simple.CONST_SEQ_MAX_LEN))
                return seq
            return ''
        else:
            return ''
    except:
        return ''

if __name__ == '__main__':
    app.run()