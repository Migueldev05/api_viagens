from sqlalchemy import String, BigInteger, Integer, VARCHAR
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class classe_model(Base):
    __tablename__ = "Classe"

    id_classe: Mapped[int] = MappedColumn(Integer, primary_key=True)
    nome_classe: Mapped[str] = MappedColumn(VARCHAR(45))
    fator_preco: Mapped[int] = MappedColumn(Integer)