from flask import Flask, render_template, request
from flasgger import Swagger

# Session 3
app = Flask(__name__)
Swagger(app)

#Session 1
#@app.route("/")
#def base_route():
    #return ("Hello  World")

# Session 3
#@app.route("/")
#def base_route():
    #return render_template("home.html")

#Session 3
@app.route("/")
def base_route():
    return "Welcome to Praxis"

#Session 3
@app.route("/hello", methods=["GET"])
def hello():
    """ Lets Create some swagger app
    --------
    parameters:
        - name: number1
        in: query
        type: number
        required: true
        - name: name1
        in: query
        type: string
        required: true 
    responses:
      200:
        description: The result is     
    """

    # These values are independent of Above parameters.
    # In absence of above paramenters We can input these values thorugh postman or "?" mark
    number1 = request.args.get("number1")   
    name1 = request.args.get("name1")
    return f"The Number is {number1} and the Name is {name1}"

#Session 2
#@app.route("/hello/<name>")
#def hello(name):
    #return f"hello {name}"

#Session 2
#@app.route("/test/<int:number>", methods= ["POST", "GET"])
#def test(number):
    #if number <= 10:
        #return f"test {number}", 200
    #if number >= 11:
        #return f"test {number}", 206

#Session 2
#@app.route("/flt/<float:numb>")
#def flt(numb):
    #return f"flt {numb}"


if __name__ == "__main__":
    app.run( debug=True)
 





