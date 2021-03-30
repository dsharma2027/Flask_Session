from flask import Flask, render_template, request 
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)


@app.route("/")
def base_route(): 
    # return render_template("home.html")
    return "Welcome to Praxis"

# @app.route("/hello/<float:number>", methods=["GET"])
@app.route("/hello",methods=["GET"])
def hello(): 
        
    """Let's try Swagger from flasgger
    ---
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
    number1 = request.args.get("number1")
    name1 = request.args.get("name1")

    return f"The number is {number1} and the name is {name1}"

if __name__ == "__main__":
    app.run()