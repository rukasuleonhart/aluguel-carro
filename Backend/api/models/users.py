from datetime import datetime
from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import UniqueConstraint, func

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    telefone: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())