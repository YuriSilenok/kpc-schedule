from fastapi import FastAPI
import models

app = FastAPI()

@app.get("/groups")
async def read_root():
    result = {
        'count':0,
        'entities':[],
    }
    for group in models.Group.select():
        result['count'] += 1
        result['entities'].append({
            'id': group.id,
            'name': group.name,
        })
    return result