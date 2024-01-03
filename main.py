import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

git_value = "Github main branch"
outer_value = os.environ.get("FROM_ARGO", "Not from Argo")

@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@app.get("/value/git")
def read_git():
    return git_value


@app.get("/value/argo")
def read_git():
    return outer_value