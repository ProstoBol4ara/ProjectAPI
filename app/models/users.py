from models.base import *


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (
        ForeignKeyConstraint(["created_by"], ["users.user_id"], name="users_fkey"),
        ForeignKeyConstraint(["deleted_by"], ["users.user_id"], name="users_fkey1"),
        ForeignKeyConstraint(["user_id"], ["users.user_id"], name="users_fkey2"),
        PrimaryKeyConstraint("user_id", name="users_pkey"),
        UniqueConstraint("email", name="users_email_key"),
        UniqueConstraint("username", name="users_username_key"),
    )

    user_id = mapped_column(Integer, autoincrement=True)
    username = mapped_column(String(100), nullable=False)
    email = mapped_column(String(255), nullable=False)
    password_hash = mapped_column(Text, nullable=False)
    created_at = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = mapped_column(Boolean, server_default=text("false"))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional["Users"]] = relationship(
        "Users",
        remote_side=[user_id],
        foreign_keys=[created_by],
        back_populates="users_reverse",
    )
    users_reverse: Mapped[List["Users"]] = relationship(
        "Users",
        uselist=True,
        remote_side=[created_by],
        foreign_keys=[created_by],
        back_populates="users",
    )
    users_: Mapped[Optional["Users"]] = relationship(
        "Users",
        remote_side=[user_id],
        foreign_keys=[deleted_by],
        back_populates="users__reverse",
    )
    users__reverse: Mapped[List["Users"]] = relationship(
        "Users",
        uselist=True,
        remote_side=[deleted_by],
        foreign_keys=[deleted_by],
        back_populates="users_",
    )
    actors: Mapped[List["Actors"]] = relationship(
        "Actors",
        uselist=True,
        foreign_keys="[Actors.created_by]",
        back_populates="users",
    )
    actors_: Mapped[List["Actors"]] = relationship(
        "Actors",
        uselist=True,
        foreign_keys="[Actors.deleted_by]",
        back_populates="users_",
    )
    content: Mapped[List["Content"]] = relationship(
        "Content",
        uselist=True,
        foreign_keys="[Content.created_by]",
        back_populates="users",
    )
    content_: Mapped[List["Content"]] = relationship(
        "Content",
        uselist=True,
        foreign_keys="[Content.deleted_by]",
        back_populates="users_",
    )
    countries: Mapped[List["Countries"]] = relationship(
        "Countries",
        uselist=True,
        foreign_keys="[Countries.created_by]",
        back_populates="users",
    )
    countries_: Mapped[List["Countries"]] = relationship(
        "Countries",
        uselist=True,
        foreign_keys="[Countries.deleted_by]",
        back_populates="users_",
    )
    coupons: Mapped[List["Coupons"]] = relationship(
        "Coupons",
        uselist=True,
        foreign_keys="[Coupons.created_by]",
        back_populates="users",
    )
    coupons_: Mapped[List["Coupons"]] = relationship(
        "Coupons",
        uselist=True,
        foreign_keys="[Coupons.deleted_by]",
        back_populates="users_",
    )
    directors: Mapped[List["Directors"]] = relationship(
        "Directors",
        uselist=True,
        foreign_keys="[Directors.created_by]",
        back_populates="users",
    )
    directors_: Mapped[List["Directors"]] = relationship(
        "Directors",
        uselist=True,
        foreign_keys="[Directors.deleted_by]",
        back_populates="users_",
    )
    genres: Mapped[List["Genres"]] = relationship(
        "Genres",
        uselist=True,
        foreign_keys="[Genres.created_by]",
        back_populates="users",
    )
    genres_: Mapped[List["Genres"]] = relationship(
        "Genres",
        uselist=True,
        foreign_keys="[Genres.deleted_by]",
        back_populates="users_",
    )
    languages: Mapped[List["Languages"]] = relationship(
        "Languages",
        uselist=True,
        foreign_keys="[Languages.created_by]",
        back_populates="users",
    )
    languages_: Mapped[List["Languages"]] = relationship(
        "Languages",
        uselist=True,
        foreign_keys="[Languages.deleted_by]",
        back_populates="users_",
    )
    notifications: Mapped[List["Notifications"]] = relationship(
        "Notifications",
        uselist=True,
        foreign_keys="[Notifications.created_by]",
        back_populates="users",
    )
    notifications_: Mapped[List["Notifications"]] = relationship(
        "Notifications",
        uselist=True,
        foreign_keys="[Notifications.deleted_by]",
        back_populates="users_",
    )
    notifications1: Mapped[List["Notifications"]] = relationship(
        "Notifications",
        uselist=True,
        foreign_keys="[Notifications.user_id]",
        back_populates="user",
    )
    payment_methods: Mapped[List["PaymentMethods"]] = relationship(
        "PaymentMethods",
        uselist=True,
        foreign_keys="[PaymentMethods.created_by]",
        back_populates="users",
    )
    payment_methods_: Mapped[List["PaymentMethods"]] = relationship(
        "PaymentMethods",
        uselist=True,
        foreign_keys="[PaymentMethods.deleted_by]",
        back_populates="users_",
    )
    payment_methods1: Mapped[List["PaymentMethods"]] = relationship(
        "PaymentMethods",
        uselist=True,
        foreign_keys="[PaymentMethods.user_id]",
        back_populates="user",
    )
    roles: Mapped[List["Roles"]] = relationship(
        "Roles", uselist=True, foreign_keys="[Roles.created_by]", back_populates="users"
    )
    roles_: Mapped[List["Roles"]] = relationship(
        "Roles",
        uselist=True,
        foreign_keys="[Roles.deleted_by]",
        back_populates="users_",
    )
    subscription_plans: Mapped[List["SubscriptionPlans"]] = relationship(
        "SubscriptionPlans",
        uselist=True,
        foreign_keys="[SubscriptionPlans.created_by]",
        back_populates="users",
    )
    subscription_plans_: Mapped[List["SubscriptionPlans"]] = relationship(
        "SubscriptionPlans",
        uselist=True,
        foreign_keys="[SubscriptionPlans.deleted_by]",
        back_populates="users_",
    )
    content_actors: Mapped[List["ContentActors"]] = relationship(
        "ContentActors",
        uselist=True,
        foreign_keys="[ContentActors.created_by]",
        back_populates="users",
    )
    content_actors_: Mapped[List["ContentActors"]] = relationship(
        "ContentActors",
        uselist=True,
        foreign_keys="[ContentActors.deleted_by]",
        back_populates="users_",
    )
    content_countries: Mapped[List["ContentCountries"]] = relationship(
        "ContentCountries",
        uselist=True,
        foreign_keys="[ContentCountries.created_by]",
        back_populates="users",
    )
    content_countries_: Mapped[List["ContentCountries"]] = relationship(
        "ContentCountries",
        uselist=True,
        foreign_keys="[ContentCountries.deleted_by]",
        back_populates="users_",
    )
    content_directors: Mapped[List["ContentDirectors"]] = relationship(
        "ContentDirectors",
        uselist=True,
        foreign_keys="[ContentDirectors.created_by]",
        back_populates="users",
    )
    content_directors_: Mapped[List["ContentDirectors"]] = relationship(
        "ContentDirectors",
        uselist=True,
        foreign_keys="[ContentDirectors.deleted_by]",
        back_populates="users_",
    )
    content_genres: Mapped[List["ContentGenres"]] = relationship(
        "ContentGenres",
        uselist=True,
        foreign_keys="[ContentGenres.created_by]",
        back_populates="users",
    )
    content_genres_: Mapped[List["ContentGenres"]] = relationship(
        "ContentGenres",
        uselist=True,
        foreign_keys="[ContentGenres.deleted_by]",
        back_populates="users_",
    )
    content_languages: Mapped[List["ContentLanguages"]] = relationship(
        "ContentLanguages",
        uselist=True,
        foreign_keys="[ContentLanguages.created_by]",
        back_populates="users",
    )
    content_languages_: Mapped[List["ContentLanguages"]] = relationship(
        "ContentLanguages",
        uselist=True,
        foreign_keys="[ContentLanguages.deleted_by]",
        back_populates="users_",
    )
    episodes: Mapped[List["Episodes"]] = relationship(
        "Episodes",
        uselist=True,
        foreign_keys="[Episodes.created_by]",
        back_populates="users",
    )
    episodes_: Mapped[List["Episodes"]] = relationship(
        "Episodes",
        uselist=True,
        foreign_keys="[Episodes.deleted_by]",
        back_populates="users_",
    )
    favorites: Mapped[List["Favorites"]] = relationship(
        "Favorites",
        uselist=True,
        foreign_keys="[Favorites.created_by]",
        back_populates="users",
    )
    favorites_: Mapped[List["Favorites"]] = relationship(
        "Favorites",
        uselist=True,
        foreign_keys="[Favorites.deleted_by]",
        back_populates="users_",
    )
    favorites1: Mapped[List["Favorites"]] = relationship(
        "Favorites",
        uselist=True,
        foreign_keys="[Favorites.user_id]",
        back_populates="user",
    )
    pay_per_view: Mapped[List["PayPerView"]] = relationship(
        "PayPerView",
        uselist=True,
        foreign_keys="[PayPerView.created_by]",
        back_populates="users",
    )
    pay_per_view_: Mapped[List["PayPerView"]] = relationship(
        "PayPerView",
        uselist=True,
        foreign_keys="[PayPerView.deleted_by]",
        back_populates="users_",
    )
    reviews: Mapped[List["Reviews"]] = relationship(
        "Reviews",
        uselist=True,
        foreign_keys="[Reviews.created_by]",
        back_populates="users",
    )
    reviews_: Mapped[List["Reviews"]] = relationship(
        "Reviews",
        uselist=True,
        foreign_keys="[Reviews.deleted_by]",
        back_populates="users_",
    )
    reviews1: Mapped[List["Reviews"]] = relationship(
        "Reviews", uselist=True, foreign_keys="[Reviews.user_id]", back_populates="user"
    )
    user_roles: Mapped["UserRoles"] = relationship(
        "UserRoles",
        uselist=False,
        foreign_keys="[UserRoles.created_by]",
        back_populates="users",
    )
    user_roles_: Mapped[List["UserRoles"]] = relationship(
        "UserRoles",
        uselist=True,
        foreign_keys="[UserRoles.deleted_by]",
        back_populates="users_",
    )
    user_roles1: Mapped[List["UserRoles"]] = relationship(
        "UserRoles",
        uselist=True,
        foreign_keys="[UserRoles.user_id]",
        back_populates="user",
    )
    user_subscriptions: Mapped[List["UserSubscriptions"]] = relationship(
        "UserSubscriptions",
        uselist=True,
        foreign_keys="[UserSubscriptions.created_by]",
        back_populates="users",
    )
    user_subscriptions_: Mapped[List["UserSubscriptions"]] = relationship(
        "UserSubscriptions",
        uselist=True,
        foreign_keys="[UserSubscriptions.deleted_by]",
        back_populates="users_",
    )
    user_subscriptions1: Mapped[List["UserSubscriptions"]] = relationship(
        "UserSubscriptions",
        uselist=True,
        foreign_keys="[UserSubscriptions.user_id]",
        back_populates="user",
    )
    watch_history: Mapped[List["WatchHistory"]] = relationship(
        "WatchHistory",
        uselist=True,
        foreign_keys="[WatchHistory.created_by]",
        back_populates="users",
    )
    watch_history_: Mapped[List["WatchHistory"]] = relationship(
        "WatchHistory",
        uselist=True,
        foreign_keys="[WatchHistory.deleted_by]",
        back_populates="users_",
    )
    watch_history1: Mapped[List["WatchHistory"]] = relationship(
        "WatchHistory",
        uselist=True,
        foreign_keys="[WatchHistory.user_id]",
        back_populates="user",
    )
    payments: Mapped[List["Payments"]] = relationship(
        "Payments",
        uselist=True,
        foreign_keys="[Payments.created_by]",
        back_populates="users",
    )
    payments_: Mapped[List["Payments"]] = relationship(
        "Payments",
        uselist=True,
        foreign_keys="[Payments.deleted_by]",
        back_populates="users_",
    )
