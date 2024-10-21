from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import ContentLanguages

router = APIRouter(
    prefix="/content_languages",
    tags=["content_languages"]
)

@router.get('/')
async def get_content_languages(db: Session = Depends(get_db)):
    content_languages = db.query(ContentLanguages).all()
    if content_languages is None:
        raise HTTPException(status_code=400, detail="Content languages not found")
    return [{"content_language_id": content_language.content_language_id, "content_id": content_language.content_id, "language_id": content_language.language_id} for content_language in content_languages]

@router.get('/{content_language_id}')
async def get_content_language(content_language_id: int, db: Session = Depends(get_db)):
    content_language = db.query(ContentLanguages).filter(ContentLanguages.content_language_id == content_language_id).first()
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")
    return {"content_language_id": content_language.content_language_id, "content_id": content_language.content_id, "language_id": content_language.language_id}

@router.post('/')
async def create_content_language(content_id: int, language_id: int, db: Session = Depends(get_db)):
    try:
        new_content_language = ContentLanguages(content_id=content_id, language_id=language_id)
        db.add(new_content_language)
        db.commit()
        db.refresh(new_content_language)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_language_id": new_content_language.content_language_id, "content_id": new_content_language.content_id, "language_id": new_content_language.language_id}

@router.put('/{content_language_id}')
async def update_content_language(content_language_id: int, content_id: int = None, language_id: int = None, db: Session = Depends(get_db)):
    content_language = db.query(ContentLanguages).filter(ContentLanguages.content_language_id == content_language_id).first()
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")

    if content_id:
        content_language.email = content_id
    if language_id:
        content_language.language_id = language_id

    db.commit()
    db.refresh(content_language)
    return {"content_language_id": content_language.id, "content_id": content_language.content_id, "language_id": content_language.language_id}

@router.delete('/{content_language_id}')
async def delete_content_language(content_language_id: int, db: Session = Depends(get_db)):
    content_language = db.query(ContentLanguages).filter(ContentLanguages.content_language_id == content_language_id).first()
    if content_language is None:
        raise HTTPException(status_code=400, detail="Content language not found")

    db.delete(content_language)
    db.commit()
    return {"message": "Content language deleted successfully"}