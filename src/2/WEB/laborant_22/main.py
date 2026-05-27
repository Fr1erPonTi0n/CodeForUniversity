import uvicorn
from api import router as api_router
from rest import router as rest_router
from fastapi import FastAPI
from app_lifespan import lifespan


app = FastAPI(title='Books',
              lifespan=lifespan)

app.include_router(rest_router)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


