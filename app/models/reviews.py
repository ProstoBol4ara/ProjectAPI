from models.base import *

class Reviews(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='reviews_rating_check'),
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='reviews_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='reviews_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='reviews_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='reviews_user_id_fkey'),
        PrimaryKeyConstraint('review_id', name='reviews_pkey')
    )

    review_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    rating = mapped_column(SmallInteger)
    comment = mapped_column(Text)
    review_date = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='reviews')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='reviews')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='reviews_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='reviews1')
