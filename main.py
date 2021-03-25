from flask import Flask

app = Flask(__name__)

@app.route("/")
def base_route():
    return "hello world"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"

@app.route("/test/<int:number>")
def test(number):
    if number <= 10:
        return f"test {number}", 200
    if number >= 11:
        return f"test {number}", 206

@app.route("/flt/<float:numb>")
def flt(numb):
    return f"flt {numb}"


if __name__ == "__main__":
    app.run( debug=True)
 





