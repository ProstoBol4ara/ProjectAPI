from models.base import *


class Coupons(Base):
    __tablename__ = "coupons"
    __table_args__ = (
        CheckConstraint(
            "discount_percentage >= 0::numeric AND discount_percentage <= 100::numeric",
            name="coupons_discount_percentage_check",
        ),
        ForeignKeyConstraint(
            ["created_by"], ["users.user_id"], name="coupons_created_by_fkey"
        ),
        ForeignKeyConstraint(
            ["deleted_by"], ["users.user_id"], name="coupons_deleted_by_fkey"
        ),
        PrimaryKeyConstraint("coupon_id", name="coupons_pkey"),
        UniqueConstraint("code", name="coupons_code_key"),
    )

    coupon_id = mapped_column(BigInteger, autoincrement=True)
    code = mapped_column(String(50), nullable=False)
    discount_percentage = mapped_column(Numeric(5, 2), nullable=False)
    valid_from = mapped_column(Date)
    valid_until = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_at = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[created_by], back_populates="coupons"
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users", foreign_keys=[deleted_by], back_populates="coupons_"
    )
