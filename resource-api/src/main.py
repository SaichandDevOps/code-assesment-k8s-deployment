
from fastapi.exceptions import HTTPException
from typing import Optional
from fastapi import FastAPI
from src.states import states

app = FastAPI()


@app.get("/")
def read_root():
    return {"Using Fast API"}


"""
    + GET [/name-by-state-code]
    + parameter : Optional
        - code : str 
    + Request : /name-by-state-code?code=oh
    + Response :  "Ohio"
"""

@app.get("/name-by-state-code")
def get_item(code: Optional[str]=None):
    state_by_code = {value:key for key, value in states.items()}
    if code:
        code = code.upper()
        if code in state_by_code:
            return state_by_code[code]
    raise HTTPException(status_code=404, detail = "state name not found.")



        
