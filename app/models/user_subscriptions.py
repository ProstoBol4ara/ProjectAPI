from models.base import *

class UserSubscriptions(Base):
    __tablename__ = 'user_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='user_subscriptions_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='user_subscriptions_deleted_by_fkey'),
        ForeignKeyConstraint(['plan_id'], ['subscription_plans.plan_id'], name='user_subscriptions_plan_id_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_subscriptions_user_id_fkey'),
        PrimaryKeyConstraint('user_subscription_id', name='user_subscriptions_pkey')
    )

    user_subscription_id = mapped_column(Integer, autoincrement=True)
    start_date = mapped_column(Date, nullable=False)
    end_date = mapped_column(Date, nullable=False)
    user_id = mapped_column(Integer)
    plan_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='user_subscriptions')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='user_subscriptions_')
    plan: Mapped[Optional['SubscriptionPlans']] = relationship('SubscriptionPlans', back_populates='user_subscriptions')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='user_subscriptions1')
