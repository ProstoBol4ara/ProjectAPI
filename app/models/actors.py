from models.base import *

class Actors(Base):
    __tablename__ = 'actors'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='actors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='actors_deleted_by_fkey'),
        PrimaryKeyConstraint('actor_id', name='actors_pkey')
    )

    actor_id = mapped_column(Integer, autoincrement=True)
    actor_name = mapped_column(String(255), nullable=False)
    biography = mapped_column(Text)
    birth_date = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='actors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='actors_')
    content_actors: Mapped[List['ContentActors']] = relationship('ContentActors', uselist=True, back_populates='actor')
