from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_something():
    """A simple test api endpoint

    Returns:
        simple_string: simple_description
    """
    return {"msg": "Hello World"}
