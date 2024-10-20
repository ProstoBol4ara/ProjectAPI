from models.base import *

class UserRoles(Base):
    __tablename__ = 'user_roles'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='user_roles_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='user_roles_deleted_by_fkey'),
        ForeignKeyConstraint(['role_id'], ['roles.role_id'], name='user_roles_role_id_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_roles_user_id_fkey'),
        PrimaryKeyConstraint('user_role_id', name='user_roles_pkey'),
        UniqueConstraint('created_by', name='user_roles_key')
    )

    user_role_id = mapped_column(Integer, autoincrement=True)
    user_id = mapped_column(Integer)
    role_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='user_roles')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='user_roles_')
    role: Mapped[Optional['Roles']] = relationship('Roles', back_populates='user_roles')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='user_roles1')
