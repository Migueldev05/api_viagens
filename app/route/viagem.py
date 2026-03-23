from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import veiculo
from app.models import passageiro
from app.models.avaliacao import AvaliacaoModel
from app.models.classe import ClasseModel
from app.models.corrida import CorridaModel
from app.models.metodo_pagamento import MetodoPagamentoModel
from app.models.modelo_veiculo import Modeloveiculomodel
from app.models.motorista_veiculo import MotoristaVeiculoModel
from app.models.motorista import MotoristaModel
from app.models.pagamentos import PagamentoModel
from app.models.passageiro import PassageiroModel
from app.models.servico import ServicoModel
from app.models.tipo_combustivel import tipo_combustivel_model
from app.models.usuario import UsuarioModel
from app.models.veiculo import VeiculoModel
from app.schema.avaliacao import AvaliacaoSchema
from app.schema.classe import ClasseSchema
from app.schema.corrida import CorridaSchema
from app.schema.metodo_pagamento import MetodoPagamentoSchema
from app.schema.modelo import ModeloSchema
from app.schema.motorista_veiculo import MotoristaVeiculoSchema
from app.schema.motorista import MotoristaSchema
from app.schema.pagamento import PagamentoSchema
from app.schema.passageiro import PassageiroSchema
from app.schema.servico import ServicoSchema
from app.schema.usuario import UsuarioSchema
from app.schema.veiculo import VeiculoSchema


avaliacao = APIRouter()
classe = APIRouter()

@avaliacao.get("/avaliacao")
async def avaliar(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    avaliar_corrida = AvaliacaoModel(**dados.model_dump())
    pass


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


