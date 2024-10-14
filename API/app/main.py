from fastapi import FastAPI, status, HTTPException
import uvicorn

films: list = ["Duna", "Avatar", "Duna 2"]
numbers: list = [2, 3, 5, 1, 6, 10]

app = FastAPI()

@app.get("/api/{index}")
def select_once(index: int):
    if(index < 0 or index >= len(films)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not correct index")
    return {'film name': films[index]}

@app.get("/api/find_by_name/")
def find_by_name(name: str):
    return {'count film\'s': films.count(name)}

@app.get("/api/")
def get_all(sortStrategy: int = None):
    match(sortStrategy):
        case None:
            return {'status': status.HTTP_200_OK, 'list': numbers}
        case 1:
            return {'status': status.HTTP_200_OK, 'list': sorted(numbers)}
        case -1:
            return {'status': status.HTTP_200_OK, 'list': sorted(numbers, reverse=True)}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not correct index")

@app.get("/api/get_film/")
def get_films():
    return films

@app.post("/api/")
def add(name: str):
    if name.strip() == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not correct name")
    return status.HTTP_200_OK

@app.put("/api/")
def update(index: int, name: str):
    if(index < 0 or index >= len(films)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not correct index")
    films[index] = name
    return status.HTTP_200_OK

@app.delete("/api/")
def delete(index: int):
    if(index < 0 or index >= len(films)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not correct index")
    films.pop(index)
    return status.HTTP_200_OK

if __name__ == '__main__':
    uvicorn.run(app)