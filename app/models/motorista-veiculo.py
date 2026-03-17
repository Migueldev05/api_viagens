from sqlalchemy.orm import MappedColumn, Mapped
from app.database import Base
from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, CHAR, SMALLINT, SmallInteger
from decimal import Decimal

class motorista_veiculo_model(Base):
    __tablename__ = "Motorista_Veiculo"

    id_motorista: Mapped[int] = MappedColumn(Integer, Primary_key=True, ForeignKey=True)
    id_veiculo: Mapped[int] = MappedColumn(Integer, Primary_key=True, ForeignKey=True)
    datahora_inicio : Mapped[DateTime] = MappedColumn(DateTime)
    datahora_fim : Mapped[DateTime] = MappedColumn(DateTime)