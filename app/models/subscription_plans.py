from models.base import *

class SubscriptionPlans(Base):
    __tablename__ = 'subscription_plans'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='subscription_plans_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='subscription_plans_deleted_by_fkey'),
        PrimaryKeyConstraint('plan_id', name='subscription_plans_pkey')
    )

    plan_id = mapped_column(Integer)
    plan_name = mapped_column(String(255), nullable=False)
    plan_price = mapped_column(Numeric(10, 2))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='subscription_plans')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='subscription_plans_')
    user_subscriptions: Mapped[List['UserSubscriptions']] = relationship('UserSubscriptions', uselist=True, back_populates='plan')
