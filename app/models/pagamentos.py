from sqlalchemy import BigInteger, ForeignKey, Integer, DateTime, SmallInteger
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class pagamentos_model(Base):
    __tablaname__ = "Pagamentos"

    id_pagamentos: Mapped[int] = MappedColumn(BigInteger, Primary_key=True)
    id_corrida: Mapped[int] = MappedColumn(BigInteger, ForeignKey=True, Unique=True)
    valor: Mapped[int] = MappedColumn(Integer)
    id_metodo_pagamento: Mapped[int] = MappedColumn(SmallInteger, ForeignKey=True, Unique=True)
    datahora_transacao: Mapped[int] = MappedColumn(DateTime)