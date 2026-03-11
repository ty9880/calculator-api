from fastapi import FastAPI, status, HTTPException, Depends
from google.cloud import bigquery
import math

app = FastAPI()

# Dependency method to provide a BigQuery client
# This will be used by the other endpoints where a database connection is necessary
def get_bq_client():
    # client automatically uses Cloud Run's service account credentials
    client = bigquery.Client()
    try:
        yield client
    finally:
        client.close()


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


@app.get("/dbwritetest", status_code=200)
def dbwritetest(bq: bigquery.Client = Depends(get_bq_client)):
    """
    Writes a simple test row to a BigQuery table.

    Uses the `get_bq_client` dependency method to establish a connection to BigQuery.
    """
    # Define a Python list of objects that will become rows in the database table
    # In this instance, there is only a single object in the list
    row_to_insert = [
        {
            "endpoint": "/dbwritetest",
            "result": "Success",
            "status_code": 200
        }
    ]
    
    # Use the BigQuery interface to write our data to the table
    # If there are errors, store them in a list called `errors`
    # YOU MUST UPDATE YOUR PROJECT AND DATASET NAME BELOW BEFORE THIS WILL WORK!!!
    errors = bq.insert_rows_json("mgmt54500-sp26-dev-tucci.calculator.api_logs", row_to_insert)

    # If there were any errors, raise an HTTPException to inform the user
    if errors:
        # Log the full error to your Cloud Run logs for debugging
        print(f"BigQuery Insert Errors: {errors}")
        
        # Raise an exception to the API user
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Failed to log data to BigQuery",
                "errors": errors  # Optional: return specific BQ error details
            }
        )

    # If there were NOT any errors, send a friendly response message to the API caller
    return {"message": "Log entry created successfully"}
