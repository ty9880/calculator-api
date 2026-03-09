from fastapi import FastAPI, status, HTTPException
import math

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")
    return {"result": a + b}


@app.get("/subtract/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Subtracting two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Multiplying two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Dividing two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a / b}

@app.get("/power/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Raises a number to a power.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a ** b}


@app.get("/sqrt/{a}", status_code=200)
def sqrt(a: float):
    """
    Calculates the square root of a number.
    
    Parameters:
    - a: Number to find the square root of
    
    Returns:
    - JSON object with the result
    """
    return {"result": math.sqrt(a)}


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: float, b: float, c: float):
    """
    Calculates the average of two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    - c: Third number
    
    Returns:
    - JSON object with the result
    """
    return {"result": (a+b+c) / 3}
