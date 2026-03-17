from sqlalchemy.orm import MappedColumn, Mapped
from app.database import Base
from sqlalchemy import BigInteger, ForeignKey, Integer
from decimal import Decimal

class motorista_model(Base):
    __tablename__ = "Motorista"

    id_motorista: Mapped[int] = MappedColumn(Integer, Primary_Key=True,)
    id_usuario: Mapped[int] = MappedColumn(BigInteger, ForeignKey=True, Unique=True)
    media_avaliacap: Mapped[int] = MappedColumn(Integer)
    cnh: Mapped[int] = MappedColumn(BigInteger)