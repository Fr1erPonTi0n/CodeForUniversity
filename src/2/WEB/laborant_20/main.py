import uvicorn
from api import router as api_router
from api.main_views import router as main_router
from fastapi import FastAPI


app = FastAPI(title='Books')

app.include_router(main_router)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


