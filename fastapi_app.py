from fastapi  import FastAPI

app = FastAPI(
    Title="FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0"
)


@app.get("/")
def welcome():
    return "Welcome to the AI&ML course!"


@app.get("/intro")
def intro():
    return "Welcome to the FastAPI application!"


@app.get("/main")
def main():
    return "This is the main function of the FastAPI application."




