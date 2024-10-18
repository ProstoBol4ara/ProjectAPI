from models.base import *

class ContentDirectors(Base):
    __tablename__ = 'content_directors'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_directors_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_directors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_directors_deleted_by_fkey'),
        ForeignKeyConstraint(['director_id'], ['directors.director_id'], name='content_directors_director_id_fkey'),
        PrimaryKeyConstraint('content_director_id', name='content_directors_pkey')
    )

    content_director_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    director_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_directors')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_directors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_directors_')
    director: Mapped[Optional['Directors']] = relationship('Directors', back_populates='content_directors')
