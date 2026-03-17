from sqlalchemy import String, BigInteger, Integer, Nullable, DateTime, SmallInteger, CHAR, VARCHAR
from sqlalchemy.orm import Mapped, MappedColumn
from app.database import Base


class Usuario_model(Base):
    __tablename__ = "Usuario"

    id_usuario: Mapped[int] = MappedColumn(BigInteger, Primary_Key=True, auto_increment=True)
    nome: Mapped[str] = MappedColumn(Integer, Text=True)
    cpf: Mapped[str] = MappedColumn(CHAR(11), Unique=True)
    data_nascimento: Mapped[DateTime] = MappedColumn(DateTime, Nullable=False)
    idade: Mapped[int] = MappedColumn(SmallInteger, )
    senha: Mapped[str] = MappedColumn(String, )
    email: Mapped[str] = MappedColumn(String, Unique=True)
    usuario: Mapped[str] = MappedColumn(VARCHAR(50), Unique=True)
