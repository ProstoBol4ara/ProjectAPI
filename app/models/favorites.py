from models.base import *

class Favorites(Base):
    __tablename__ = 'favorites'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='favorites_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='favorites_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='favorites_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='favorites_user_id_fkey'),
        PrimaryKeyConstraint('favorite_id', name='favorites_pkey')
    )

    favorite_id = mapped_column(Integer, autoincrement=True)
    user_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    added_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='favorites')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='favorites')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='favorites_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='favorites1')
