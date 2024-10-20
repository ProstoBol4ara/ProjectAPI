from models.base import *

class ContentCountries(Base):
    __tablename__ = 'content_countries'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_countries_content_id_fkey'),
        ForeignKeyConstraint(['country_id'], ['countries.country_id'], name='content_countries_country_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_countries_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_countries_deleted_by_fkey'),
        PrimaryKeyConstraint('content_country_id', name='content_countries_pkey')
    )

    content_country_id = mapped_column(Integer, autoincrement=True)
    content_id = mapped_column(Integer)
    country_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_countries')
    country: Mapped[Optional['Countries']] = relationship('Countries', back_populates='content_countries')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_countries')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_countries_')
