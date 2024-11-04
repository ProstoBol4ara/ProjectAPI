from models.base import *


class Genres(Base):
    __tablename__ = "genres"
    __table_args__ = (
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="genres_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="genres_deleted_by_fkey"
        ),
        PrimaryKeyConstraint("genre_id", name="genres_pkey"),
    )

    genre_id = mapped_column(Integer, autoincrement=True)
    genre_name = mapped_column(String(100), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="genres"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="genres_"
    )
    content_genres: Mapped[List["ContentGenres"]] = relationship(
        "ContentGenres", uselist=True, back_populates="genre"
    )
