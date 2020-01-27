
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HOLA!!, te paseo'

#en localhost:5000
if __name__ == "__main__":
    app.run()