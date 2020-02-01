from flask import Flask
app=Flask(__name__)


@app.route("/")
def home():
    return "This is home page releasing on 25th"

if __name__=="__main__":
    app.run(debug=True)
