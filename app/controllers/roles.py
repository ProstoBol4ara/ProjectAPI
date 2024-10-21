from fastapi import APIRouter, HTTPException, Depends
from database import get_db, Session
from models import Roles

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@router.get('/')
async def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Roles).all()
    if roles is None:
        raise HTTPException(status_code=400, detail="Roles not found")
    return [{"role_id": role.role_id, "role_name": role.role_name} for role in roles]

@router.get('/{role_id}')
async def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Roles).filter(Roles.role_id == role_id).first()
    if role is None:
        raise HTTPException(status_code=400, detail="Role not found")
    return {"role_id": role.role_id, "role_name": role.role_name}

@router.post('/')
async def create_role(role_name: str, db: Session = Depends(get_db)):
    try:
        new_role = Roles(role_name=role_name)
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
    except:
        raise HTTPException(status_code=400, detail="Create failed")
    return {"role_id": new_role.role_id, "role_name": new_role.role_name}

@router.put('/{role_id}')
async def update_role(role_id: int, role_name: str = None, db: Session = Depends(get_db)):
    role = db.query(Roles).filter(Roles.role_id == role_id).first()
    if role is None:
        raise HTTPException(status_code=400, detail="Role not found")

    if role_name:
        role.role_name = role_name

    db.commit()
    db.refresh(role)
    return {"role_id": role.role_id, "role_name": role.role_name}

@router.delete('/{role_id}')
async def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Roles).filter(Roles.role_id == role_id).first()
    if role is None:
        raise HTTPException(status_code=400, detail="Role not found")

    db.delete(role)
    db.commit()
    return {"message": "Role deleted successfully"}