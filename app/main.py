# HELLO FASTAPI

# create a fastapi application that returns "Hello FastAPI" when you visit the root URL
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}



# create a fastapi application that has one endpoint /user/{username}. When accessing the endpoint it returns a JSON response with information about the user (name, second name, years, email), that are stored in a dcitionary. If the user does not exist, it returns a 404 error.



users = {
    "slavko": {
        "name": "Slavko",
        "second_name": "Slavkic",
        "years": 68,
        "email": "slavko68@email.com"},
    "mirko": {
        "name": "Mirko",
        "second_name": "Mirkic",
        "years": 55,
        "email": "nemammail@com"}
    }

@app.get("/user/{username}")
async def get_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[username]

# create a pydantic model named Article using BaseModel. This model should represent attributes with name, description, price and quantity.


class Article(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# create a fastAPI endpoint /artciles that uses Article as an entry parameters. Checks the data against the model and returns all the data in form of JSON with details about the article.
@app.get("/articles")
async def get_articles(article: Article):
    return article

# create a new fast api endpoint /get_articles which returns all the articles from the list
articles = [
    {
        "name": "article1",
        "description": "description1",
        "price": 10.0,
        "quantity": 1
    },
    {
        "name": "article2",
        "description": "description2",
        "price": 20.0,
        "quantity": 2
    },
    {
        "name": "article3",
        "description": "description3",
        "price": 30.0,
        "quantity": 3
    }
]
@app.get("/get_articles")
async def get_all_articles():
    return articles
