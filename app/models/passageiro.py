from sqlalchemy.orm import MappedColumn, Mapped
from app.database import Base
from sqlalchemy import BigInteger, ForeignKey, Integer
from decimal import Decimal

class passageiro_model(Base):
    __tablename__ = "Passageiro"

    id_passageiro: Mapped[int] = MappedColumn(Integer, Primary_Key=True,)
    id_usuario: Mapped[int] = MappedColumn(BigInteger, ForeignKey=True, Unique=True)
    media_avaliacap: Mapped[int] = MappedColumn(Integer)
    