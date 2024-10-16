SET check_function_bodies = false;

CREATE TABLE actors(
  actor_id serial NOT NULL,
  actor_name varchar(255) NOT NULL,
  biography text,
  birth_date date,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT actors_pkey PRIMARY KEY(actor_id)
);

CREATE TABLE "content"(
  content_id serial NOT NULL,
  title varchar(255) NOT NULL,
  preview_path text,
  description text,
  release_date date,
  content_type varchar(50)
  CHECK (content_type IN ('Movie', 'TV Show', 'Documentary')),
  content_path text,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_pkey PRIMARY KEY(content_id)
);

CREATE TABLE content_actors(
  content_actor_id serial NOT NULL,
  content_id integer,
  actor_id integer,
  "role" varchar(255),
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_actors_pkey PRIMARY KEY(content_actor_id)
);

CREATE TABLE content_countries(
  content_country_id serial NOT NULL,
  content_id integer,
  country_id integer,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_countries_pkey PRIMARY KEY(content_country_id)
);

CREATE TABLE content_directors(
  content_director_id serial NOT NULL,
  content_id integer,
  director_id integer,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_directors_pkey PRIMARY KEY(content_director_id)
);

CREATE TABLE content_genres(
  content_genre_id serial NOT NULL,
  content_id integer,
  genre_id integer,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_genres_pkey PRIMARY KEY(content_genre_id)
);

CREATE TABLE content_languages(
  content_language_id serial NOT NULL,
  content_id integer,
  language_id integer,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT content_languages_pkey PRIMARY KEY(content_language_id)
);

CREATE TABLE countries(
  country_id serial NOT NULL,
  country_name varchar(255) NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp DEFAULT CURRENT_TIMESTAMP,
  deleted_by integer,
  CONSTRAINT countries_pkey PRIMARY KEY(country_id)
);

CREATE TABLE coupons(
  coupon_id serial8 NOT NULL,
  code varchar(50) NOT NULL UNIQUE,
  discount_percentage numeric(5, 2) NOT NULL
  CHECK (discount_percentage >= 0 AND discount_percentage <= 100),
  valid_from date,
  valid_until date,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT coupons_pkey PRIMARY KEY(coupon_id)
);

CREATE TABLE directors(
  director_id serial NOT NULL,
  director_name varchar(255) NOT NULL,
  biography text,
  birth_date date,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT directors_pkey PRIMARY KEY(director_id)
);

CREATE TABLE episodes(
  episode_id serial NOT NULL,
  content_id integer,
  season_number integer,
  episode_number integer,
  title varchar(255),
  release_date date,
  episode_path text,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT episodes_pkey PRIMARY KEY(episode_id)
);

CREATE TABLE favorites(
  favorite_id serial NOT NULL,
  user_id integer,
  content_id integer,
  added_at timestamp DEFAULT CURRENT_TIMESTAMP,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT favorites_pkey PRIMARY KEY(favorite_id)
);

CREATE TABLE genres(
  genre_id serial NOT NULL,
  genre_name varchar(100) NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT genres_pkey PRIMARY KEY(genre_id)
);

CREATE TABLE languages(
  language_id serial NOT NULL,
  language_name varchar(100) NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT languages_pkey PRIMARY KEY(language_id)
);

CREATE TABLE notifications(
  notification_id serial NOT NULL,
  user_id integer,
  message text NOT NULL,
  notification_date timestamp DEFAULT CURRENT_TIMESTAMP,
  is_read boolean DEFAULT FALSE,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT notifications_pkey PRIMARY KEY(notification_id)
);

CREATE TABLE pay_per_view(
  pay_per_view_id integer NOT NULL,
  content_id integer,
  amount numeric(10, 2) NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT pay_per_view_pkey PRIMARY KEY(pay_per_view_id)
);

CREATE TABLE payment_methods(
  payment_method_id serial NOT NULL,
  user_id integer,
  method_type varchar(50)
  CHECK (method_type IN ('Credit Card', 'Bank Transfer', 'SBP')),
  provider varchar(255),
  account_number varchar(50),
  expiry_date date,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT payment_methods_pkey PRIMARY KEY(payment_method_id)
);

CREATE TABLE payments(
  payment_id serial NOT NULL,
  payment_date timestamp DEFAULT CURRENT_TIMESTAMP,
  payment_method_id integer,
  pay_per_view_id integer,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT payments_key UNIQUE(payment_id)
);

CREATE TABLE reviews(
  review_id serial NOT NULL,
  content_id integer,
  user_id integer,
  rating int2 CHECK (rating BETWEEN 1 AND 5),
  "comment" text,
  review_date timestamp DEFAULT CURRENT_TIMESTAMP,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT reviews_pkey PRIMARY KEY(review_id)
);

CREATE TABLE roles(
  role_id serial NOT NULL,
  role_name varchar(50) NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT roles_pkey PRIMARY KEY(role_id)
);

CREATE TABLE subscription_plans(
  plan_id serial NOT NULL,
  plan_name varchar(255) NOT NULL,
  plan_price numeric(10, 2),
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT subscription_plans_pkey PRIMARY KEY(plan_id)
);

CREATE TABLE user_roles(
  user_role_id serial NOT NULL,
  user_id int4,
  role_id int4,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT user_roles_pkey PRIMARY KEY(user_role_id),
  CONSTRAINT user_roles_key UNIQUE(created_by)
);

CREATE TABLE user_subscriptions(
  user_subscription_id serial NOT NULL,
  user_id integer,
  plan_id integer,
  start_date date NOT NULL,
  end_date date NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT user_subscriptions_pkey PRIMARY KEY(user_subscription_id)
);

CREATE TABLE users(
  user_id serial NOT NULL,
  username varchar(100) NOT NULL UNIQUE,
  email varchar(255) NOT NULL UNIQUE,
  password_hash text NOT NULL,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT users_pkey PRIMARY KEY(user_id)
);

CREATE TABLE watch_history(
  watch_history_id serial NOT NULL,
  user_id integer,
  content_id integer,
  watched_at timestamp DEFAULT CURRENT_TIMESTAMP,
  is_deleted boolean DEFAULT FALSE,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  created_by integer,
  deleted_at timestamp,
  deleted_by integer,
  CONSTRAINT watch_history_pkey PRIMARY KEY(watch_history_id)
);

ALTER TABLE users
  ADD CONSTRAINT users_fkey FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE users
  ADD CONSTRAINT users_fkey1 FOREIGN KEY (deleted_by) REFERENCES users (user_id)
  ;

ALTER TABLE roles
  ADD CONSTRAINT roles_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE roles
  ADD CONSTRAINT roles_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE user_roles
  ADD CONSTRAINT user_roles_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE user_roles
  ADD CONSTRAINT user_roles_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE user_roles
  ADD CONSTRAINT user_roles_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE user_roles
  ADD CONSTRAINT user_roles_role_id_fkey
    FOREIGN KEY (role_id) REFERENCES roles (role_id);

ALTER TABLE "content"
  ADD CONSTRAINT content_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE "content"
  ADD CONSTRAINT content_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE episodes
  ADD CONSTRAINT episodes_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE episodes
  ADD CONSTRAINT episodes_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE episodes
  ADD CONSTRAINT episodes_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE genres
  ADD CONSTRAINT genres_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE genres
  ADD CONSTRAINT genres_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_genres
  ADD CONSTRAINT content_genres_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE content_genres
  ADD CONSTRAINT content_genres_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_genres
  ADD CONSTRAINT content_genres_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE content_genres
  ADD CONSTRAINT content_genres_genre_id_fkey
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id);

ALTER TABLE actors
  ADD CONSTRAINT actors_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE actors
  ADD CONSTRAINT actors_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_actors
  ADD CONSTRAINT content_actors_actor_id_fkey
    FOREIGN KEY (actor_id) REFERENCES actors (actor_id);

ALTER TABLE content_actors
  ADD CONSTRAINT content_actors_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE content_actors
  ADD CONSTRAINT content_actors_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE content_actors
  ADD CONSTRAINT content_actors_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE directors
  ADD CONSTRAINT directors_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE directors
  ADD CONSTRAINT directors_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_directors
  ADD CONSTRAINT content_directors_director_id_fkey
    FOREIGN KEY (director_id) REFERENCES directors (director_id);

ALTER TABLE content_directors
  ADD CONSTRAINT content_directors_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE content_directors
  ADD CONSTRAINT content_directors_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE content_directors
  ADD CONSTRAINT content_directors_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE user_subscriptions
  ADD CONSTRAINT user_subscriptions_plan_id_fkey
    FOREIGN KEY (plan_id) REFERENCES subscription_plans (plan_id);

ALTER TABLE subscription_plans
  ADD CONSTRAINT subscription_plans_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE subscription_plans
  ADD CONSTRAINT subscription_plans_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE user_subscriptions
  ADD CONSTRAINT user_subscriptions_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE user_subscriptions
  ADD CONSTRAINT user_subscriptions_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE user_subscriptions
  ADD CONSTRAINT user_subscriptions_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE payment_methods
  ADD CONSTRAINT payment_methods_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE payment_methods
  ADD CONSTRAINT payment_methods_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE payment_methods
  ADD CONSTRAINT payment_methods_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE payments
  ADD CONSTRAINT payments_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE payments
  ADD CONSTRAINT payments_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE payments
  ADD CONSTRAINT payments_payment_method_id_fkey
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods (payment_method_id)
  ;

ALTER TABLE users
  ADD CONSTRAINT users_fkey2 FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE reviews
  ADD CONSTRAINT reviews_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE reviews
  ADD CONSTRAINT reviews_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE reviews
  ADD CONSTRAINT reviews_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE reviews
  ADD CONSTRAINT reviews_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE watch_history
  ADD CONSTRAINT watch_history_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE watch_history
  ADD CONSTRAINT watch_history_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE watch_history
  ADD CONSTRAINT watch_history_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE watch_history
  ADD CONSTRAINT watch_history_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE favorites
  ADD CONSTRAINT favorites_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE favorites
  ADD CONSTRAINT favorites_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE favorites
  ADD CONSTRAINT favorites_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE favorites
  ADD CONSTRAINT favorites_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE notifications
  ADD CONSTRAINT notifications_user_id_fkey
    FOREIGN KEY (user_id) REFERENCES users (user_id);

ALTER TABLE notifications
  ADD CONSTRAINT notifications_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE notifications
  ADD CONSTRAINT notifications_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE countries
  ADD CONSTRAINT countries_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE countries
  ADD CONSTRAINT countries_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_countries
  ADD CONSTRAINT content_countries_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE content_countries
  ADD CONSTRAINT content_countries_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_countries
  ADD CONSTRAINT content_countries_country_id_fkey
    FOREIGN KEY (country_id) REFERENCES countries (country_id);

ALTER TABLE content_countries
  ADD CONSTRAINT content_countries_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE languages
  ADD CONSTRAINT languages_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE languages
  ADD CONSTRAINT languages_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_languages
  ADD CONSTRAINT content_languages_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE content_languages
  ADD CONSTRAINT content_languages_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE content_languages
  ADD CONSTRAINT content_languages_language_id_fkey
    FOREIGN KEY (language_id) REFERENCES languages (language_id);

ALTER TABLE content_languages
  ADD CONSTRAINT content_languages_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE coupons
  ADD CONSTRAINT coupons_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE coupons
  ADD CONSTRAINT coupons_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

ALTER TABLE pay_per_view
  ADD CONSTRAINT pay_per_view_content_id_fkey
    FOREIGN KEY (content_id) REFERENCES "content" (content_id);

ALTER TABLE payments
  ADD CONSTRAINT payments_pay_per_view_id_fkey
    FOREIGN KEY (pay_per_view_id) REFERENCES pay_per_view (pay_per_view_id);

ALTER TABLE pay_per_view
  ADD CONSTRAINT pay_per_view_created_by_fkey
    FOREIGN KEY (created_by) REFERENCES users (user_id);

ALTER TABLE pay_per_view
  ADD CONSTRAINT pay_per_view_deleted_by_fkey
    FOREIGN KEY (deleted_by) REFERENCES users (user_id);

