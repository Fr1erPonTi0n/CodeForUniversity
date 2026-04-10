import uvicorn
from api import router as api_router
from fastapi import FastAPI


app = FastAPI(title='Books')

app.include_router(api_router)


@app.get('/')
def read_root():
    return {
        'message': '/docs',
    }

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


