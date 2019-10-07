from flask import Flask , request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    try:
        print(data['res'])
    except:
        print("error")
    return "running"



if __name__ == "__main__":
    app.run(debug=True)