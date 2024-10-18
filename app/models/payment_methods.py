from models.base import *

class PaymentMethods(Base):
    __tablename__ = 'payment_methods'
    __table_args__ = (
        CheckConstraint("method_type::text = ANY (ARRAY['Credit Card'::character varying, 'Bank Transfer'::character varying, 'SBP'::character varying]::text[])", name='payment_methods_method_type_check'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='payment_methods_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='payment_methods_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='payment_methods_user_id_fkey'),
        PrimaryKeyConstraint('payment_method_id', name='payment_methods_pkey')
    )

    payment_method_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    method_type = mapped_column(String(50))
    provider = mapped_column(String(255))
    account_number = mapped_column(String(50))
    expiry_date = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='payment_methods')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='payment_methods_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='payment_methods1')
    payments: Mapped[List['Payments']] = relationship('Payments', uselist=True, back_populates='payment_method')

