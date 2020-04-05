from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/ola")
def ola():
    return "Czesc tu ola"

@app.route("/platforma")
def platfroma():
    return "<img src = 'pixel.gif'>"
    
if __name__ == "__main__":
    app.run(debug=True)