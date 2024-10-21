from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Languages

router = APIRouter(
    prefix="/languages",
    tags=["languages"]
)

@router.get('/')
async def get_languages(db: Session = Depends(get_db)):
    languages = db.query(Languages).all()
    if languages is None:
        raise HTTPException(status_code=400, detail="Languages not found")
    return [{"language_id": language.language_id, "name": language.language_name} for language in languages]

@router.get('/{language_id}')
async def get_language(language_id: int, db: Session = Depends(get_db)):
    language = db.query(Languages).filter(Languages.language_id == language_id).first()
    if language is None:
        raise HTTPException(status_code=400, detail="Language not found")
    return {"language_id": language.language_id, "name": language.language_name}

@router.post('/')
async def create_language(language_name: str, db: Session = Depends(get_db)):
    try:
        new_language = Languages(language_name=language_name)
        db.add(new_language)
        db.commit()
        db.refresh(new_language)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"language_id": new_language.language_id, "name": new_language.language_name}

@router.put('/{language_id}')
async def update_language(language_id: int, language_name: str = None, db: Session = Depends(get_db)):
    language = db.query(Languages).filter(Languages.language_id == language_id).first()
    if language is None:
        raise HTTPException(status_code=400, detail="Language not found")

    if language_name:
        language.language_name = language_name

    db.commit()
    db.refresh(language)
    return {"language_id": language.language_id, "name": language.language_name}

@router.delete('/{language_id}')
async def delete_language(language_id: int, db: Session = Depends(get_db)):
    language = db.query(Languages).filter(Languages.language_id == language_id).first()
    if language is None:
        raise HTTPException(status_code=400, detail="Language not found")

    db.delete(language)
    db.commit()
    return {"message": "Language deleted successfully"}