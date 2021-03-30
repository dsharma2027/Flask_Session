# from flask import Flask, request
# from flasgger import Swagger

import uvicorn  #ASGI Support
from fastapi import FastAPI


#app = Flask(__name__)
app = FastAPI()

#Swagger(app)


#@app.route("/")

@app.get('/')
def base_route(): 
    # return render_template("home.html")
    return "Welcome to Praxis"

# @app.route("/hello/<float:number>", methods=["GET"])
#@app.route("/hello",methods=["GET"])

@app.get("/hello")
def hello(name1:str): 
        
    # """Let's try Swagger from flasgger
    # ---
    # parameters:  
    #   - name: number1
    #     in: query
    #     type: number
    #     required: true
    #   - name: name1
    #     in: query
    #     type: string
    #     required: true
    # responses:
    #     200:
    #         description: The result is
    #     """
   
    return f"The name is {name1}"

if __name__ == "__main__":
    # app.run()
    uvicorn.run(app)
    