from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Categorie(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)


class Plat(Base):
    __tablename__ = "plats"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(150), nullable=False)
    prix: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    categorie_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    telephone: Mapped[str | None] = mapped_column(String(30))


class Commande(Base):
    __tablename__ = "commandes"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    date_commande: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)


class CommandePlat(Base):
    __tablename__ = "commande_plats"

    commande_id: Mapped[int] = mapped_column(
        ForeignKey("commandes.id"), primary_key=True
    )
    plat_id: Mapped[int] = mapped_column(ForeignKey("plats.id"), primary_key=True)
    quantite: Mapped[int] = mapped_column(nullable=False)


class Fournisseur(Base):
    __tablename__ = "fournisseurs"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(150), nullable=False)
    contact: Mapped[str] = mapped_column(String(150))


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(150), nullable=False)
    cout_unitaire: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    fournisseur_id: Mapped[int] = mapped_column(
        ForeignKey("fournisseurs.id"), nullable=False
    )


class PlatIngredient(Base):
    __tablename__ = "plat_ingredients"

    plat_id: Mapped[int] = mapped_column(ForeignKey("plats.id"), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"), primary_key=True
    )
    quantite_necessaire: Mapped[Decimal] = mapped_column(
        Numeric(10, 3), nullable=False
    )


class Avis(Base):
    __tablename__ = "avis"
    __table_args__ = (
        CheckConstraint("note BETWEEN 1 AND 5", name="check_note"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    plat_id: Mapped[int] = mapped_column(ForeignKey("plats.id"), nullable=False)
    note: Mapped[int] = mapped_column(nullable=False)
    commentaire: Mapped[str | None] = mapped_column(Text)
    date_avis: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )


engine = create_engine(
    "postgresql+psycopg2://postgres:Darkavatar.31@localhost:5432/restaurant_db",
    echo=True,
)

Base.metadata.create_all(engine)

