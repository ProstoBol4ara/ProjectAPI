from models.base import *

class Content(Base):
    __tablename__ = 'content'
    __table_args__ = (
        CheckConstraint("content_type::text = ANY (ARRAY['Movie'::character varying, 'TV Show'::character varying, 'Documentary'::character varying]::text[])", name='content_content_type_check'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_deleted_by_fkey'),
        PrimaryKeyConstraint('content_id', name='content_pkey')
    )

    content_id = mapped_column(Integer)
    title = mapped_column(String(255), nullable=False)
    preview_path = mapped_column(Text)
    description = mapped_column(Text)
    release_date = mapped_column(Date)
    content_type = mapped_column(String(50))
    content_path = mapped_column(Text)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_')
    content_actors: Mapped[List['ContentActors']] = relationship('ContentActors', uselist=True, back_populates='content')
    content_countries: Mapped[List['ContentCountries']] = relationship('ContentCountries', uselist=True, back_populates='content')
    content_directors: Mapped[List['ContentDirectors']] = relationship('ContentDirectors', uselist=True, back_populates='content')
    content_genres: Mapped[List['ContentGenres']] = relationship('ContentGenres', uselist=True, back_populates='content')
    content_languages: Mapped[List['ContentLanguages']] = relationship('ContentLanguages', uselist=True, back_populates='content')
    episodes: Mapped[List['Episodes']] = relationship('Episodes', uselist=True, back_populates='content')
    favorites: Mapped[List['Favorites']] = relationship('Favorites', uselist=True, back_populates='content')
    pay_per_view: Mapped[List['PayPerView']] = relationship('PayPerView', uselist=True, back_populates='content')
    reviews: Mapped[List['Reviews']] = relationship('Reviews', uselist=True, back_populates='content')
    watch_history: Mapped[List['WatchHistory']] = relationship('WatchHistory', uselist=True, back_populates='content')
