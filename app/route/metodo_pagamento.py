from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import session
from app.database import get_db
from app.model.metodo_pagamento import MetodoPagamentoModel
from app.schema.metodo_pagamento import MetodoPagamentoSchema, MetodoPagamentoUpdateSchema

metodopagamento = APIRouter()

