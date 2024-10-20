from models.base import *

class Notifications(Base):
    __tablename__ = 'notifications'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='notifications_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='notifications_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='notifications_user_id_fkey'),
        PrimaryKeyConstraint('notification_id', name='notifications_pkey')
    )

    notification_id = mapped_column(Integer, autoincrement=True)
    message = mapped_column(Text, nullable=False)
    user_id = mapped_column(Integer)
    notification_date = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_read = mapped_column(Boolean, server_default=text('false'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='notifications')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='notifications_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='notifications1')
