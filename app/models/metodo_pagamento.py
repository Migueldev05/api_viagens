from sqlalchemy import VARCHAR, SmallInteger
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class metodo_pagamento_model(Base):
    __tablename__ = "Metodo_Pagameto"

    id_metodo_pagamento: Mapped[int] = MappedColumn(SmallInteger, Primary_key=True)
    descricao: Mapped[str] = MappedColumn(VARCHAR(45))
    nome_financeira: Mapped[str] = MappedColumn(VARCHAR(45))