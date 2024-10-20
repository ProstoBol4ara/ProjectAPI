from fastapi import APIRouter
from controllers.roles import router as roles_router
from controllers.users import router as users_router
from controllers.actors import router as actors_router
from controllers.genres import router as genres_router
from controllers.reviews import router as reviews_router
from controllers.content import router as content_router
from controllers.coupons import router as coupons_router
from controllers.payments import router as payments_router
from controllers.episodes import router as episodes_router
from controllers.countries import router as countries_router
from controllers.directors import router as directors_router
from controllers.favorites import router as favorites_router
from controllers.languages import router as languages_router
from controllers.user_roles import router as user_roles_router
from controllers.pay_per_view import router as pay_per_view_router
from controllers.notifications import router as notifications_router
from controllers.watch_history import router as watch_history_router
from controllers.content_actors import router as content_actors_router
from controllers.content_genres import router as content_genres_router
from controllers.payment_methods import router as payment_methods_router
from controllers.content_languages import router as content_languages_router
from controllers.content_countries import router as content_countries_router
from controllers.content_directors import router as content_directors_router
from controllers.subscription_plans import router as subscription_plans_router
from controllers.user_subscriptions import router as user_subscriptions_router

router = APIRouter(
    prefix="/api"
)

router.include_router(roles_router)
router.include_router(users_router)
router.include_router(actors_router)
router.include_router(genres_router)
router.include_router(reviews_router)
router.include_router(content_router)
router.include_router(coupons_router)
router.include_router(payments_router)
router.include_router(episodes_router)
router.include_router(countries_router)
router.include_router(directors_router)
router.include_router(favorites_router)
router.include_router(languages_router)
router.include_router(user_roles_router)
router.include_router(pay_per_view_router)
router.include_router(notifications_router)
router.include_router(watch_history_router)
router.include_router(content_actors_router)
router.include_router(content_genres_router)
router.include_router(payment_methods_router)
router.include_router(content_languages_router)
router.include_router(content_countries_router)
router.include_router(content_directors_router)
router.include_router(subscription_plans_router)
router.include_router(user_subscriptions_router)