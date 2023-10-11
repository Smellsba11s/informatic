from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

@app.get('/{path}')
def get_path(title:str):
    return wikipedia.search(title,1)

@app.get('/multi/{path}')
def get_multipath(count:int,title:str):
    return wikipedia.search(title,count)


class Topic(BaseModel):
    title:str
    count:int

class Summary(BaseModel):
    topic:str
    summary:str

@app.post('/',response_model=Summary)
def summary_title(topic: Topic):
    return Summary(topic = topic.title, summary = wikipedia.summary(topic.title, sentences = topic.count))
#Python (programming language) запрос