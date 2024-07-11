from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World Thien haha", "url": "root", "test": "test k8s deployment with setting imagePullPolicy: Always"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=4000, host='0.0.0.0')
