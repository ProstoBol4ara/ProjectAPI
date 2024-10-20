from models.base import *

class Episodes(Base):
    __tablename__ = 'episodes'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='episodes_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='episodes_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='episodes_deleted_by_fkey'),
        PrimaryKeyConstraint('episode_id', name='episodes_pkey')
    )

    episode_id = mapped_column(Integer, autoincrement=True)
    content_id = mapped_column(Integer)
    season_number = mapped_column(Integer)
    episode_number = mapped_column(Integer)
    title = mapped_column(String(255))
    release_date = mapped_column(Date)
    episode_path = mapped_column(Text)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='episodes')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='episodes')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='episodes_')
