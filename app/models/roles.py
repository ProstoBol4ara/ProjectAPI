from models.base import *


class Roles(Base):
    __tablename__ = "roles"
    __table_args__ = (
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="roles_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="roles_deleted_by_fkey"
        ),
        PrimaryKeyConstraint("role_id", name="roles_pkey"),
    )

    role_id = mapped_column(Integer, autoincrement=True)
    role_name = mapped_column(String(50), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="roles"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="roles_"
    )
    user_roles: Mapped[List["UserRoles"]] = relationship(
        "UserRoles", uselist=True, back_populates="role"
    )
