from models.base import *

class Countries(Base):
    __tablename__ = 'countries'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='countries_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='countries_deleted_by_fkey'),
        PrimaryKeyConstraint('country_id', name='countries_pkey')
    )

    country_id = mapped_column(Integer, autoincrement=True)
    country_name = mapped_column(String(255), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='countries')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='countries_')
    content_countries: Mapped[List['ContentCountries']] = relationship('ContentCountries', uselist=True, back_populates='country')
