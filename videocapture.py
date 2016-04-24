from flask import Flask, request, render_template, Response, abort, send_from_directory
from flask.json import jsonify
from datetime import datetime
from os import listdir
from os.path import join, exists
app = Flask(__name__)


VID_DIR = '/Users/vorlenko/workspace/videocapture/media'


@app.route('/', methods=['GET'])
def home():
    fnames = reversed(sorted([f for f in listdir(VID_DIR) if f.endswith('.mp4')]))
    return render_template('home.html', fnames=fnames), 200

@app.route('/video/<fname>')
def videofile(fname):
    if exists(join(VID_DIR, fname)):
        return send_from_directory(VID_DIR, fname)
    abort(404)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['thefile']
    vidtype = request.form['vidtype']
    composer = request.form['composer']
    piece = request.form['piece']
    date = datetime.now()
    fname = '-'.join((date.strftime('%Y-%m-%d-%H-%M-%S'), vidtype, composer, piece))
    f.save('%s/%s.mp4' % (VID_DIR, fname))
    return jsonify(fname=fname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
