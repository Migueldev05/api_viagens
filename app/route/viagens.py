from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

from app.model.classe import ClasseModel
from app.schema.classe import ClasseSchema



classe = APIRouter()


@classe.post("/classe")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    nova_classe = ClasseModel(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe.delete("/classe/{id}")
async def deletar_classe(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    
    db.delete(classe)
    db.commit()

    return {"mensagem": "Sua classe foi deletada!"}



