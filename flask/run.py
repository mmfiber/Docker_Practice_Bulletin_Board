from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!!"

if __name__ == '__main__':
  # host should be '0.0.0.0'
  # http://flask.pocoo.org/docs/0.12/quickstart/
  app.run(host='0.0.0.0', port=5000, debug=True)