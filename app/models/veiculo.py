from sqlalchemy.orm import MappedColumn, Mapped
from app.database import Base
from sqlalchemy import BigInteger, ForeignKey, Integer, CHAR, SMALLINT, SmallInteger
from decimal import Decimal

class veiculo_model(Base):
    __tablename__ = "Viculo"

    id_veiculo: Mapped[int] = MappedColumn(Integer, Primary_Key=True)
    placa: Mapped[str] = MappedColumn(CHAR(7))
    id_modelo: Mapped[int] = MappedColumn(Integer, ForeignKey=True, Unique=True)
    tem_seguro: Mapped[int] = MappedColumn(SmallInteger)
    id_classe: Mapped[int] = MappedColumn(Integer, ForeignKey=True, Unique=True)