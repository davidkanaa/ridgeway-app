from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routes import router

app = FastAPI(title="Ridgeway HVAC Mock API")


@app.exception_handler(RequestValidationError)
async def custom_form_validation_error_handler(
    request: Request, exc: RequestValidationError
):
    custom_errors = []

    # Iterate through default error structures
    for error in exc.errors():
        field_name = error.get("loc")[-1] if error.get("loc") else "unknown"

        custom_errors.append(
            {
                "field": field_name,
                "error_type": error.get("type"),
                "message": error.get("msg").capitalize(),
            }
        )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Schema validation failed.", "errors": custom_errors},
    )


app.include_router(router)
