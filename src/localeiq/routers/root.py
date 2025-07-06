from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    """
    Returns the welcome statement
    FIXME: move to datasource
    """
    return {"message": "Welcome to LocaleIQ"}
