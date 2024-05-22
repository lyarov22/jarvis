from flask import Flask, render_template, redirect, url_for

import pc_control as pcc

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mute', methods=['POST'])
def mute():
    pcc.volumeMute()
    return redirect(url_for('index'))


@app.route('/unmute', methods=['POST'])
def unmute():
    pcc.volumeUp()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
