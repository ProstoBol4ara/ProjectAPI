from models.base import *


class Languages(Base):
    __tablename__ = "languages"
    __table_args__ = (
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="languages_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="languages_deleted_by_fkey"
        ),
        PrimaryKeyConstraint("language_id", name="languages_pkey"),
    )

    language_id = mapped_column(Integer, autoincrement=True)
    language_name = mapped_column(String(100), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="languages"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="languages_"
    )
    content_languages: Mapped[List["ContentLanguages"]] = relationship(
        "ContentLanguages", uselist=True, back_populates="language"
    )
