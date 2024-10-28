from fastapi import HTTPException
from functools import wraps

def handle_exceptions(status_code=400):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as ex:
                raise HTTPException(status_code=status_code, detail=str(ex))
        return wrapper
    return decorator
