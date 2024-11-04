from models.base import *


class WatchHistory(Base):
    __tablename__ = "watch_history"
    __table_args__ = (
        ForeignKeyConstraint(
            ["content_id"], ["content.content_id"], name="watch_history_content_id_fkey"
        ),
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="watch_history_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="watch_history_deleted_by_fkey"
        ),
        ForeignKeyConstraint(
            ["user_id"], ["users.user_id"], name="watch_history_user_id_fkey"
        ),
        PrimaryKeyConstraint("watch_history_id", name="watch_history_pkey"),
    )

    watch_history_id = mapped_column(Integer, autoincrement=True)
    user_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    watched_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional["Content"]] = relationship(
        "Content", back_populates="watch_history"
    )
    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="watch_history"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="watch_history_"
    )
    user: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[user_id], back_populates="watch_history1"
    )
