"""
This is a sample FastAPI application that defines a single endpoint at the root URL ("/").
When accessed, it returns a JSON response with a message "Hello World!".

To create the web server, you can run this script using Uvicorn.
Make sure you have FastAPI and Uvicorn installed in your Python environment.

Run using the command in the terminal:
    uvicorn main:app
"""

"""
The decorator @app.get("/") in FastAPI is used to define a route for the HTTP GET
method at the root URL ("/"). When a client sends a GET request to the root URL,
the function read_root() will be executed, and its return value will be sent back as the response.
In this case, it returns a JSON object with a message "Hello World!".
"""

# name of library: FastAPI
from fastapi import Body, FastAPI

#instance of FastAPI class
app = FastAPI()

# path operations #
# The `async` keyword means the method can pause while waiting for something else
# while waiting the app can do other things instead of being stuck
# helping the server handle more requests at the same time
# decorator turns function into a path operation that can be accessed via HTTP GET request at the root URL ("/")
@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

# pass in decorator to define a new route for the HTTP GET method at the URL "/posts"
@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

# decorator tells FastAPI to handle HTTP POST requests to /createposts
# payload:dict means FastAPI should request the body to be parsed as a dictionary
# (fastapi method) Body = (...) tells FastAPI the body is required, if no JSON data is sent validation error occurs
# prints received data to terminal where app is running
# return sends JSON back to client
@app.post("/createposts")
def create_posts(payload: dict = Body(...)): # 3 dots means it is required if not, it would be 'None' instead
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}

