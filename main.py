import flask
app = flask.Flask(__name__)

items = {"PC":"Custom-Built PC with pre-chosen parts", "Macbook":"Apple's hit new PC - just like last years, but 0.1% faster!", "Yogabook":"For those who don't want a tablet"}

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/stuff/<item>')
def lookup(item):
    if item in items:
        return flask.render_template('index.html', item = item, definition = items[item])
    else:
        return flask.render_template('index.html', item = 'not found', definition = "item doesn't exist")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)