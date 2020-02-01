from flask import Flask
app=Flask(__name__)

@app.route("/about")
def about():
    return "this is about page releasing on 25th"

if __name__=="__main__":
    app.run(debug=True)
