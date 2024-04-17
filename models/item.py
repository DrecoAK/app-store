from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    __table_args__ = (db.UniqueConstraint("name", "store_id"),)

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String(80), unique=False, nullable=False)
    price: db.Mapped[float] = db.mapped_column(
        db.Float(precision=2), unique=False, nullable=False
    )
    store_id = db.mapped_column(
        db.ForeignKey("stores.id"), unique=False, nullable=False
    )

    store = db.relationship("StoreModel", back_populates="items")
