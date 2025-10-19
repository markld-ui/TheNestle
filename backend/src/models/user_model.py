from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
   pass


class UserOrm(Model):
   __tablename__ = "users"
   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str]
   bio: Mapped[str | None]
   email: Mapped[str]
   age: Mapped[int]