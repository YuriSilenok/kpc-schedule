from fastapi import FastAPI
import models as m
import base_models as bm

app = FastAPI()

@app.get("/groups")
async def get_groups():
    '''Получить список групп'''
    result = {
        'count':0,
        'entities':[],
    }
    for group in m.Group.select():
        result['count'] += 1
        result['entities'].append({
            'id': group.id,
            'name': group.name,
        })
    return result

@app.post("/groups")
async def post_groups(group: bm.Group):
    '''Создать группу'''
    m.Group.create(
        name=group.name
    )
    return group
    

@app.get("/subgroups")
async def get_sub_groups():
    '''Получить список подгрупп'''
    result = {
        'count':0,
        'entities':[],
    }
    for sub_group in m.SubGroup.select():
        result['count'] += 1
        result['entities'].append({
            'id': sub_group.id,
            'name': sub_group.name,
            'grou_id': sub_group.group_id
        })
    return result