from fastapi import FastAPI
from fastapi.openapi.models import Contact, License

app = FastAPI(
    title="ProjectAPI",
    description="Туда сюда стриминг сервис",
    version="v0",
    contact=Contact(
        name="Абонент временно не доступен",
        url="https://ea.ne.clown.org/contact"
    ),
    license_info=License(
        name="Скам не иначе",
        url="https://scam.mamantov.com/license"
    )
)
