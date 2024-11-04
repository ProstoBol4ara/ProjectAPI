from models.base import *


class ContentLanguages(Base):
    __tablename__ = "content_languages"
    __table_args__ = (
        ForeignKeyConstraint(
            ["content_id"],
            ["content.content_id"],
            name="content_languages_content_id_fkey",
        ),
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="content_languages_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="content_languages_deleted_by_fkey"
        ),
        ForeignKeyConstraint(
            ["language_id"],
            ["languages.language_id"],
            name="content_languages_language_id_fkey",
        ),
        PrimaryKeyConstraint("content_language_id", name="content_languages_pkey"),
    )

    content_language_id = mapped_column(Integer, autoincrement=True)
    content_id = mapped_column(Integer)
    language_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional["Content"]] = relationship(
        "Content", back_populates="content_languages"
    )
    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="content_languages"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="content_languages_"
    )
    language: Mapped[Optional["Languages"]] = relationship(
        "Languages", back_populates="content_languages"
    )
