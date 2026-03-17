from sqlalchemy import VARCHAR, Integer
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base

class tipo_combustivel_model(Base):
    __tablename__ = "Tipo_Combustivel"

    id_combustivel: Mapped[int] = MappedColumn(Integer, Primary_key=True)
    descricao: Mapped[str] = MappedColumn(VARCHAR(45))
    fator_carbono: Mapped[int] = MappedColumn(Integer)