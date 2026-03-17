from sqlalchemy import SmallInteger, Integer, DateTime
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class avaliacao_model(Base):
    __tablename__ = "Avaliacao"

    id_avaliacao: Mapped[int] = MappedColumn(Integer, Primary_key=True)
    nota_passageiro: Mapped[int] = MappedColumn(SmallInteger)
    nota_motorista: Mapped[int] = MappedColumn(SmallInteger)
    datahora_limite: Mapped[DateTime] = MappedColumn(DateTime)