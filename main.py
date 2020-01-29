import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html', item="PC", definition="A custom-built PC (pre-chosen parts)")

#@app.route('/stuff/<item>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)