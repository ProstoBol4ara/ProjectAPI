from models.base import *

class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='payments_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='payments_deleted_by_fkey'),
        ForeignKeyConstraint(['pay_per_view_id'], ['pay_per_view.pay_per_view_id'], name='payments_pay_per_view_id_fkey'),
        ForeignKeyConstraint(['payment_method_id'], ['payment_methods.payment_method_id'], name='payments_payment_method_id_fkey'),
        PrimaryKeyConstraint('payment_id', name='payments_pkey')
    )

    payment_id = mapped_column(Integer, autoincrement=True)
    payment_date = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    payment_method_id = mapped_column(Integer)
    pay_per_view_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='payments')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='payments_')
    pay_per_view: Mapped[Optional['PayPerView']] = relationship('PayPerView', back_populates='payments')
    payment_method: Mapped[Optional['PaymentMethods']] = relationship('PaymentMethods', back_populates='payments')
