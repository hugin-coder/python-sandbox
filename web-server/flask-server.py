from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/hello/<name>')
def hello(name: str):
    return render_template('hello.html', name=name)


@app.post('/send')
def send():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
