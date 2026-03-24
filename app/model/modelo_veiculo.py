from sqlalchemy import ForeignKey, Integer, VARCHAR, DateTime, Enum
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class Modeloveiculomodel(Base):
    __tablename__ = "Modelo_Veiculo"

    id_modelo: Mapped[int] = MappedColumn(Integer, Primary_key=True)
    nome_modelo: Mapped[str] = MappedColumn(VARCHAR(45))
    cor: Mapped[str] = MappedColumn(VARCHAR(45))
    fabricante: Mapped[str] = MappedColumn(VARCHAR(45))
    ano: Mapped[int] = MappedColumn(DateTime)
    capacidade: Mapped[int] = MappedColumn(Integer)
    propriedade: Mapped[Enum] = MappedColumn(Enum("Próprio","Alugado"))
    id_combustivel: Mapped[int] = MappedColumn(Integer, ForeignKey=True, Unique=True)