from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Content

router = APIRouter(
    prefix="/contents",
    tags=["contents"]
)

@router.get('/')
async def get_contents(db: Session = Depends(get_db)):
    contents = db.query(Content).all()
    if contents is None:
        raise HTTPException(status_code=400, detail="Contents not found")
    return [{"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path} for content in contents]

@router.get('/{content_id}')
async def get_content(content_id: int, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.content_id == content_id).first()
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")
    return {"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path}

@router.post('/')
async def create_content(title: str, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: Session = Depends(get_db)):
    try:
        if not release_date is None:
            release_date = datetime.strptime(release_date, '%d.%m.%Y').date()
        new_content = Content(title=title, preview_path=preview_path, description=description, release_date=release_date, content_type=content_type, content_path=content_path)
        db.add(new_content)
        db.commit()
        db.refresh(new_content)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"content_id": new_content.content_id, "title": new_content.title, "preview_path": new_content.preview_path, "description": new_content.description, "release_date": new_content.release_date, "content_type": new_content.content_type, "content_path": new_content.content_path}

@router.put('/{content_id}')
async def update_content(content_id: int, title: str = None, preview_path: str = None, description: str = None, release_date: str = None, content_type: str = None, content_path: str = None, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.content_id == content_id).first()
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")

    if title:
        content.title = title
    if preview_path:
        content.preview_path = preview_path
    if description:
        content.description = description
    if release_date:
        content.release_date = release_date
    if content_type:
        content.content_type = content_type
    if content_path:
        content.content_path = content_path

    db.commit()
    db.refresh(content)
    return {"content_id": content.content_id, "title": content.title, "preview_path": content.preview_path, "description": content.description, "release_date": content.release_date, "content_type": content.content_type, "content_path": content.content_path}

@router.delete('/{content_id}')
async def delete_content(content_id: int, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.content_id == content_id).first()
    if content is None:
        raise HTTPException(status_code=400, detail="Content not found")

    db.delete(content)
    db.commit()
    return {"message": "Content deleted successfully"}