from models.base import *


class ContentGenres(Base):
    __tablename__ = "content_genres"
    __table_args__ = (
        ForeignKeyConstraint(
            ["content_id"],
            ["content.content_id"],
            name="content_genres_content_id_fkey",
        ),
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="content_genres_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="content_genres_deleted_by_fkey"
        ),
        ForeignKeyConstraint(
            ["genre_id"], ["genres.genre_id"], name="content_genres_genre_id_fkey"
        ),
        PrimaryKeyConstraint("content_genre_id", name="content_genres_pkey"),
    )

    content_genre_id = mapped_column(Integer, autoincrement=True)
    content_id = mapped_column(Integer)
    genre_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional["Content"]] = relationship(
        "Content", back_populates="content_genres"
    )
    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="content_genres"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="content_genres_"
    )
    genre: Mapped[Optional["Genres"]] = relationship(
        "Genres", back_populates="content_genres"
    )
