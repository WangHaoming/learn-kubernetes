from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Dockerized Flask App!</h1><p>Running on port 5000.</p>'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=False)