from fastapi import FastAPI

app = FastAPI()


# root
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/home')
def home():
    return 'You\'ve reached home !'


# params
@app.get('/{name}')
def get_name(name: str):
    return {"name": name}
