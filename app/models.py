from typing import List, Optional

from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Users(Users):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='users_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='users_fkey1'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='users_fkey2'),
        PrimaryKeyConstraint('user_id', name='users_pkey'),
        UniqueConstraint('email', name='users_email_key'),
        UniqueConstraint('username', name='users_username_key')
    )

    user_id = mapped_column(Integer)
    username = mapped_column(String(100), nullable=False)
    email = mapped_column(String(255), nullable=False)
    password_hash = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', remote_side=[user_id], foreign_keys=[created_by], back_populates='users_reverse')
    users_reverse: Mapped[List['Users']] = relationship('Users', uselist=True, remote_side=[created_by], foreign_keys=[created_by], back_populates='users')
    users_: Mapped[Optional['Users']] = relationship('Users', remote_side=[user_id], foreign_keys=[deleted_by], back_populates='users__reverse')
    users__reverse: Mapped[List['Users']] = relationship('Users', uselist=True, remote_side=[deleted_by], foreign_keys=[deleted_by], back_populates='users_')
    actors: Mapped[List['Actors']] = relationship('Actors', uselist=True, foreign_keys='[Actors.created_by]', back_populates='users')
    actors_: Mapped[List['Actors']] = relationship('Actors', uselist=True, foreign_keys='[Actors.deleted_by]', back_populates='users_')
    content: Mapped[List['Content']] = relationship('Content', uselist=True, foreign_keys='[Content.created_by]', back_populates='users')
    content_: Mapped[List['Content']] = relationship('Content', uselist=True, foreign_keys='[Content.deleted_by]', back_populates='users_')
    countries: Mapped[List['Countries']] = relationship('Countries', uselist=True, foreign_keys='[Countries.created_by]', back_populates='users')
    countries_: Mapped[List['Countries']] = relationship('Countries', uselist=True, foreign_keys='[Countries.deleted_by]', back_populates='users_')
    coupons: Mapped[List['Coupons']] = relationship('Coupons', uselist=True, foreign_keys='[Coupons.created_by]', back_populates='users')
    coupons_: Mapped[List['Coupons']] = relationship('Coupons', uselist=True, foreign_keys='[Coupons.deleted_by]', back_populates='users_')
    directors: Mapped[List['Directors']] = relationship('Directors', uselist=True, foreign_keys='[Directors.created_by]', back_populates='users')
    directors_: Mapped[List['Directors']] = relationship('Directors', uselist=True, foreign_keys='[Directors.deleted_by]', back_populates='users_')
    genres: Mapped[List['Genres']] = relationship('Genres', uselist=True, foreign_keys='[Genres.created_by]', back_populates='users')
    genres_: Mapped[List['Genres']] = relationship('Genres', uselist=True, foreign_keys='[Genres.deleted_by]', back_populates='users_')
    languages: Mapped[List['Languages']] = relationship('Languages', uselist=True, foreign_keys='[Languages.created_by]', back_populates='users')
    languages_: Mapped[List['Languages']] = relationship('Languages', uselist=True, foreign_keys='[Languages.deleted_by]', back_populates='users_')
    notifications: Mapped[List['Notifications']] = relationship('Notifications', uselist=True, foreign_keys='[Notifications.created_by]', back_populates='users')
    notifications_: Mapped[List['Notifications']] = relationship('Notifications', uselist=True, foreign_keys='[Notifications.deleted_by]', back_populates='users_')
    notifications1: Mapped[List['Notifications']] = relationship('Notifications', uselist=True, foreign_keys='[Notifications.user_id]', back_populates='user')
    payment_methods: Mapped[List['PaymentMethods']] = relationship('PaymentMethods', uselist=True, foreign_keys='[PaymentMethods.created_by]', back_populates='users')
    payment_methods_: Mapped[List['PaymentMethods']] = relationship('PaymentMethods', uselist=True, foreign_keys='[PaymentMethods.deleted_by]', back_populates='users_')
    payment_methods1: Mapped[List['PaymentMethods']] = relationship('PaymentMethods', uselist=True, foreign_keys='[PaymentMethods.user_id]', back_populates='user')
    roles: Mapped[List['Roles']] = relationship('Roles', uselist=True, foreign_keys='[Roles.created_by]', back_populates='users')
    roles_: Mapped[List['Roles']] = relationship('Roles', uselist=True, foreign_keys='[Roles.deleted_by]', back_populates='users_')
    subscription_plans: Mapped[List['SubscriptionPlans']] = relationship('SubscriptionPlans', uselist=True, foreign_keys='[SubscriptionPlans.created_by]', back_populates='users')
    subscription_plans_: Mapped[List['SubscriptionPlans']] = relationship('SubscriptionPlans', uselist=True, foreign_keys='[SubscriptionPlans.deleted_by]', back_populates='users_')
    content_actors: Mapped[List['ContentActors']] = relationship('ContentActors', uselist=True, foreign_keys='[ContentActors.created_by]', back_populates='users')
    content_actors_: Mapped[List['ContentActors']] = relationship('ContentActors', uselist=True, foreign_keys='[ContentActors.deleted_by]', back_populates='users_')
    content_countries: Mapped[List['ContentCountries']] = relationship('ContentCountries', uselist=True, foreign_keys='[ContentCountries.created_by]', back_populates='users')
    content_countries_: Mapped[List['ContentCountries']] = relationship('ContentCountries', uselist=True, foreign_keys='[ContentCountries.deleted_by]', back_populates='users_')
    content_directors: Mapped[List['ContentDirectors']] = relationship('ContentDirectors', uselist=True, foreign_keys='[ContentDirectors.created_by]', back_populates='users')
    content_directors_: Mapped[List['ContentDirectors']] = relationship('ContentDirectors', uselist=True, foreign_keys='[ContentDirectors.deleted_by]', back_populates='users_')
    content_genres: Mapped[List['ContentGenres']] = relationship('ContentGenres', uselist=True, foreign_keys='[ContentGenres.created_by]', back_populates='users')
    content_genres_: Mapped[List['ContentGenres']] = relationship('ContentGenres', uselist=True, foreign_keys='[ContentGenres.deleted_by]', back_populates='users_')
    content_languages: Mapped[List['ContentLanguages']] = relationship('ContentLanguages', uselist=True, foreign_keys='[ContentLanguages.created_by]', back_populates='users')
    content_languages_: Mapped[List['ContentLanguages']] = relationship('ContentLanguages', uselist=True, foreign_keys='[ContentLanguages.deleted_by]', back_populates='users_')
    episodes: Mapped[List['Episodes']] = relationship('Episodes', uselist=True, foreign_keys='[Episodes.created_by]', back_populates='users')
    episodes_: Mapped[List['Episodes']] = relationship('Episodes', uselist=True, foreign_keys='[Episodes.deleted_by]', back_populates='users_')
    favorites: Mapped[List['Favorites']] = relationship('Favorites', uselist=True, foreign_keys='[Favorites.created_by]', back_populates='users')
    favorites_: Mapped[List['Favorites']] = relationship('Favorites', uselist=True, foreign_keys='[Favorites.deleted_by]', back_populates='users_')
    favorites1: Mapped[List['Favorites']] = relationship('Favorites', uselist=True, foreign_keys='[Favorites.user_id]', back_populates='user')
    pay_per_view: Mapped[List['PayPerView']] = relationship('PayPerView', uselist=True, foreign_keys='[PayPerView.created_by]', back_populates='users')
    pay_per_view_: Mapped[List['PayPerView']] = relationship('PayPerView', uselist=True, foreign_keys='[PayPerView.deleted_by]', back_populates='users_')
    reviews: Mapped[List['Reviews']] = relationship('Reviews', uselist=True, foreign_keys='[Reviews.created_by]', back_populates='users')
    reviews_: Mapped[List['Reviews']] = relationship('Reviews', uselist=True, foreign_keys='[Reviews.deleted_by]', back_populates='users_')
    reviews1: Mapped[List['Reviews']] = relationship('Reviews', uselist=True, foreign_keys='[Reviews.user_id]', back_populates='user')
    user_roles: Mapped['UserRoles'] = relationship('UserRoles', uselist=False, foreign_keys='[UserRoles.created_by]', back_populates='users')
    user_roles_: Mapped[List['UserRoles']] = relationship('UserRoles', uselist=True, foreign_keys='[UserRoles.deleted_by]', back_populates='users_')
    user_roles1: Mapped[List['UserRoles']] = relationship('UserRoles', uselist=True, foreign_keys='[UserRoles.user_id]', back_populates='user')
    user_subscriptions: Mapped[List['UserSubscriptions']] = relationship('UserSubscriptions', uselist=True, foreign_keys='[UserSubscriptions.created_by]', back_populates='users')
    user_subscriptions_: Mapped[List['UserSubscriptions']] = relationship('UserSubscriptions', uselist=True, foreign_keys='[UserSubscriptions.deleted_by]', back_populates='users_')
    user_subscriptions1: Mapped[List['UserSubscriptions']] = relationship('UserSubscriptions', uselist=True, foreign_keys='[UserSubscriptions.user_id]', back_populates='user')
    watch_history: Mapped[List['WatchHistory']] = relationship('WatchHistory', uselist=True, foreign_keys='[WatchHistory.created_by]', back_populates='users')
    watch_history_: Mapped[List['WatchHistory']] = relationship('WatchHistory', uselist=True, foreign_keys='[WatchHistory.deleted_by]', back_populates='users_')
    watch_history1: Mapped[List['WatchHistory']] = relationship('WatchHistory', uselist=True, foreign_keys='[WatchHistory.user_id]', back_populates='user')
    payments: Mapped[List['Payments']] = relationship('Payments', uselist=True, foreign_keys='[Payments.created_by]', back_populates='users')
    payments_: Mapped[List['Payments']] = relationship('Payments', uselist=True, foreign_keys='[Payments.deleted_by]', back_populates='users_')


class Actors(Base):
    __tablename__ = 'actors'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='actors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='actors_deleted_by_fkey'),
        PrimaryKeyConstraint('actor_id', name='actors_pkey')
    )

    actor_id = mapped_column(Integer)
    actor_name = mapped_column(String(255), nullable=False)
    biography = mapped_column(Text)
    birth_date = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='actors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='actors_')
    content_actors: Mapped[List['ContentActors']] = relationship('ContentActors', uselist=True, back_populates='actor')


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


class Countries(Base):
    __tablename__ = 'countries'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='countries_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='countries_deleted_by_fkey'),
        PrimaryKeyConstraint('country_id', name='countries_pkey')
    )

    country_id = mapped_column(Integer)
    country_name = mapped_column(String(255), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='countries')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='countries_')
    content_countries: Mapped[List['ContentCountries']] = relationship('ContentCountries', uselist=True, back_populates='country')


class Coupons(Base):
    __tablename__ = 'coupons'
    __table_args__ = (
        CheckConstraint('discount_percentage >= 0::numeric AND discount_percentage <= 100::numeric', name='coupons_discount_percentage_check'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='coupons_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='coupons_deleted_by_fkey'),
        PrimaryKeyConstraint('coupon_id', name='coupons_pkey'),
        UniqueConstraint('code', name='coupons_code_key')
    )

    coupon_id = mapped_column(BigInteger)
    code = mapped_column(String(50), nullable=False)
    discount_percentage = mapped_column(Numeric(5, 2), nullable=False)
    valid_from = mapped_column(Date)
    valid_until = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='coupons')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='coupons_')


class Directors(Base):
    __tablename__ = 'directors'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='directors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='directors_deleted_by_fkey'),
        PrimaryKeyConstraint('director_id', name='directors_pkey')
    )

    director_id = mapped_column(Integer)
    director_name = mapped_column(String(255), nullable=False)
    biography = mapped_column(Text)
    birth_date = mapped_column(Date)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='directors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='directors_')
    content_directors: Mapped[List['ContentDirectors']] = relationship('ContentDirectors', uselist=True, back_populates='director')


class Genres(Base):
    __tablename__ = 'genres'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='genres_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='genres_deleted_by_fkey'),
        PrimaryKeyConstraint('genre_id', name='genres_pkey')
    )

    genre_id = mapped_column(Integer)
    genre_name = mapped_column(String(100), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='genres')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='genres_')
    content_genres: Mapped[List['ContentGenres']] = relationship('ContentGenres', uselist=True, back_populates='genre')


class Languages(Base):
    __tablename__ = 'languages'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='languages_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='languages_deleted_by_fkey'),
        PrimaryKeyConstraint('language_id', name='languages_pkey')
    )

    language_id = mapped_column(Integer)
    language_name = mapped_column(String(100), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='languages')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='languages_')
    content_languages: Mapped[List['ContentLanguages']] = relationship('ContentLanguages', uselist=True, back_populates='language')


class Notifications(Base):
    __tablename__ = 'notifications'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='notifications_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='notifications_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='notifications_user_id_fkey'),
        PrimaryKeyConstraint('notification_id', name='notifications_pkey')
    )

    notification_id = mapped_column(Integer)
    message = mapped_column(Text, nullable=False)
    user_id = mapped_column(Integer)
    notification_date = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_read = mapped_column(Boolean, server_default=text('false'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='notifications')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='notifications_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='notifications1')


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


class Roles(Base):
    __tablename__ = 'roles'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='roles_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='roles_deleted_by_fkey'),
        PrimaryKeyConstraint('role_id', name='roles_pkey')
    )

    role_id = mapped_column(Integer)
    role_name = mapped_column(String(50), nullable=False)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='roles')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='roles_')
    user_roles: Mapped[List['UserRoles']] = relationship('UserRoles', uselist=True, back_populates='role')


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


class ContentActors(Base):
    __tablename__ = 'content_actors'
    __table_args__ = (
        ForeignKeyConstraint(['actor_id'], ['actors.actor_id'], name='content_actors_actor_id_fkey'),
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_actors_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_actors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_actors_deleted_by_fkey'),
        PrimaryKeyConstraint('content_actor_id', name='content_actors_pkey')
    )

    content_actor_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    actor_id = mapped_column(Integer)
    role = mapped_column(String(255))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    actor: Mapped[Optional['Actors']] = relationship('Actors', back_populates='content_actors')
    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_actors')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_actors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_actors_')


class ContentCountries(Base):
    __tablename__ = 'content_countries'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_countries_content_id_fkey'),
        ForeignKeyConstraint(['country_id'], ['countries.country_id'], name='content_countries_country_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_countries_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_countries_deleted_by_fkey'),
        PrimaryKeyConstraint('content_country_id', name='content_countries_pkey')
    )

    content_country_id = mapped_column(Integer)
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


class ContentDirectors(Base):
    __tablename__ = 'content_directors'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_directors_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_directors_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_directors_deleted_by_fkey'),
        ForeignKeyConstraint(['director_id'], ['directors.director_id'], name='content_directors_director_id_fkey'),
        PrimaryKeyConstraint('content_director_id', name='content_directors_pkey')
    )

    content_director_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    director_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_directors')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_directors')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_directors_')
    director: Mapped[Optional['Directors']] = relationship('Directors', back_populates='content_directors')


class ContentGenres(Base):
    __tablename__ = 'content_genres'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_genres_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_genres_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_genres_deleted_by_fkey'),
        ForeignKeyConstraint(['genre_id'], ['genres.genre_id'], name='content_genres_genre_id_fkey'),
        PrimaryKeyConstraint('content_genre_id', name='content_genres_pkey')
    )

    content_genre_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    genre_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_genres')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_genres')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_genres_')
    genre: Mapped[Optional['Genres']] = relationship('Genres', back_populates='content_genres')


class ContentLanguages(Base):
    __tablename__ = 'content_languages'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='content_languages_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='content_languages_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='content_languages_deleted_by_fkey'),
        ForeignKeyConstraint(['language_id'], ['languages.language_id'], name='content_languages_language_id_fkey'),
        PrimaryKeyConstraint('content_language_id', name='content_languages_pkey')
    )

    content_language_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    language_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='content_languages')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='content_languages')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='content_languages_')
    language: Mapped[Optional['Languages']] = relationship('Languages', back_populates='content_languages')


class Episodes(Base):
    __tablename__ = 'episodes'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='episodes_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='episodes_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='episodes_deleted_by_fkey'),
        PrimaryKeyConstraint('episode_id', name='episodes_pkey')
    )

    episode_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    season_number = mapped_column(Integer)
    episode_number = mapped_column(Integer)
    title = mapped_column(String(255))
    release_date = mapped_column(Date)
    episode_path = mapped_column(Text)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='episodes')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='episodes')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='episodes_')


class Favorites(Base):
    __tablename__ = 'favorites'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='favorites_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='favorites_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='favorites_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='favorites_user_id_fkey'),
        PrimaryKeyConstraint('favorite_id', name='favorites_pkey')
    )

    favorite_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    added_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='favorites')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='favorites')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='favorites_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='favorites1')


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


class Reviews(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='reviews_rating_check'),
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='reviews_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='reviews_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='reviews_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='reviews_user_id_fkey'),
        PrimaryKeyConstraint('review_id', name='reviews_pkey')
    )

    review_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    rating = mapped_column(SmallInteger)
    comment = mapped_column(Text)
    review_date = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='reviews')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='reviews')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='reviews_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='reviews1')


class UserRoles(Base):
    __tablename__ = 'user_roles'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='user_roles_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='user_roles_deleted_by_fkey'),
        ForeignKeyConstraint(['role_id'], ['roles.role_id'], name='user_roles_role_id_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_roles_user_id_fkey'),
        PrimaryKeyConstraint('user_role_id', name='user_roles_pkey'),
        UniqueConstraint('created_by', name='user_roles_key')
    )

    user_role_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    role_id = mapped_column(Integer)
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='user_roles')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='user_roles_')
    role: Mapped[Optional['Roles']] = relationship('Roles', back_populates='user_roles')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='user_roles1')


class UserSubscriptions(Base):
    __tablename__ = 'user_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='user_subscriptions_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='user_subscriptions_deleted_by_fkey'),
        ForeignKeyConstraint(['plan_id'], ['subscription_plans.plan_id'], name='user_subscriptions_plan_id_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_subscriptions_user_id_fkey'),
        PrimaryKeyConstraint('user_subscription_id', name='user_subscriptions_pkey')
    )

    user_subscription_id = mapped_column(Integer)
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


class WatchHistory(Base):
    __tablename__ = 'watch_history'
    __table_args__ = (
        ForeignKeyConstraint(['content_id'], ['content.content_id'], name='watch_history_content_id_fkey'),
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='watch_history_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='watch_history_deleted_by_fkey'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='watch_history_user_id_fkey'),
        PrimaryKeyConstraint('watch_history_id', name='watch_history_pkey')
    )

    watch_history_id = mapped_column(Integer)
    user_id = mapped_column(Integer)
    content_id = mapped_column(Integer)
    watched_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    is_deleted = mapped_column(Boolean, server_default=text('false'))
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = mapped_column(Integer)
    deleted_at = mapped_column(DateTime)
    deleted_by = mapped_column(Integer)

    content: Mapped[Optional['Content']] = relationship('Content', back_populates='watch_history')
    users: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[created_by], back_populates='watch_history')
    users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[deleted_by], back_populates='watch_history_')
    user: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[user_id], back_populates='watch_history1')


class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['users.user_id'], name='payments_created_by_fkey'),
        ForeignKeyConstraint(['deleted_by'], ['users.user_id'], name='payments_deleted_by_fkey'),
        ForeignKeyConstraint(['pay_per_view_id'], ['pay_per_view.pay_per_view_id'], name='payments_pay_per_view_id_fkey'),
        ForeignKeyConstraint(['payment_method_id'], ['payment_methods.payment_method_id'], name='payments_payment_method_id_fkey'),
        PrimaryKeyConstraint('payment_id', name='payments_pkey')
    )

    payment_id = mapped_column(Integer)
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