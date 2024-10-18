from models.base import *

class PayPerView(Base):
    __tablename__ = 'pay_per_view'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='pay_per_view_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='pay_per_view_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='pay_per_view_deleted_by_fkey'),
        PrimaryKeyConstraint('pay_per_view_id', name='pay_per_view_pkey')
    )

    pay_per_view_id = mapped_column(Integer)
    amount = mapped_column(Numeric(10, 2), nullable=False)
    content_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='pay_per_view')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='pay_per_view')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='pay_per_view_')
    payments: Mapped[List['Payments']] = relationship('Payments', uselist=True, back_populates='pay_per_view')
