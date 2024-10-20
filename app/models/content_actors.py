from models.base import *

class ContentActors(Base):
    __tablename__ = 'content_actors'
    __table_args__ = (
        ForeignKeyConstraint(['actor_id'], ['actors.actor_id'], name='content_actors_actor_id_fkey'),
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_actors_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_actors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_actors_deleted_by_fkey'),
        PrimaryKeyConstraint('content_actor_id', name='content_actors_pkey')
    )

    content_actor_id = mapped_column(Integer, autoincrement=True)
    content_id = mapped_column(Integer)
    actor_id = mapped_column(Integer)
    role = mapped_column(String(255))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    actor: Mapped[Optional['Actors']] = relationship('Actors', back_populates='content_actors')
    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_actors')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_actors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_actors_')
