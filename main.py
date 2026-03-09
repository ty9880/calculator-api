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
def add(a: str, b: str):
    """
    Subtracting two numbers together.
    
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
    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Multiplying two numbers together.
    
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
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Dividing two numbers together.
    
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
    try:
        a / b
    except ZeroDivisionError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot divide by zero")
    return {"result": a / b}


@app.get("/power/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Raises a number to a power.
    
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
    return {"result": a ** b}


@app.get("/sqrt/{a}", status_code=200)
def sqrt(a: str):
    """
    Calculates the square root of a number.
    
    Parameters:
    - a: Number to find the square root of
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="'a' must be valid number")
    try:
        if a <= 0:
            raise ValueError
    except ValueError: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="'a' must be a positive number")
    return {"result": math.sqrt(a)}


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: str, b: str, c: str):
    """
    Calculates the average of two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    - c: Third number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="'a', 'b', and 'c' must be valid numbers")
    return {"result": (a+b+c) / 3}
