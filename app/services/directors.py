from repositories import DirectorsRepository
from constants import date_pattern
from re import match


class DirectorsService:
    def __init__(self, repository: DirectorsRepository):
        self.repository = repository

    async def get_all(self):
        directors = await self.repository.get_all()

        return (
            None
            if directors is None
            else [
                {
                    "director_id": director.director_id,
                    "director_name": director.director_name,
                    "biography": director.biography,
                    "birth_date": director.birth_date,
                }
                for director in directors
            ]
        )

    async def get_one(self, director_id: int):
        if not director_id:
            raise ValueError("director_id cannot be empty")

        director = await self.repository.get_one(director_id=director_id)

        if not director:
            raise ValueError("Coupon not found")

        return {
            "director_id": director.director_id,
            "director_name": director.director_name,
            "biography": director.biography,
            "birth_date": director.birth_date,
        }

    async def create(
        self, director_name: str, biography: str = None, birth_date: str = None
    ):
        if not director_name:
            raise ValueError("director_name cannot be empty")

        if not birth_date or not match(date_pattern, birth_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        new_director = await self.repository.create(
            director_name=director_name, biography=biography, birth_date=birth_date
        )

        return {
            "director_id": new_director.director_id,
            "director_name": new_director.director_name,
            "biography": new_director.biography,
            "birth_date": new_director.birth_date,
        }

    async def update(
        self,
        director_id: int,
        director_name: str = None,
        biography: str = None,
        birth_date: str = None,
    ):
        if not director_id:
            raise ValueError("director_id cannot be empty")

        if not birth_date or not match(date_pattern, birth_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        director = await self.repository.update(
            director_id=director_id,
            director_name=director_name,
            biography=biography,
            birth_date=birth_date,
        )

        if not director:
            raise ValueError("Director not found")

        return {
            "director_id": director.director_id,
            "director_name": director.director_name,
            "biography": director.biography,
            "birth_date": director.birth_date,
        }

    async def delete(self, director_id: int):
        if not director_id:
            raise ValueError("director_id cannot be empty")

        if not (
            delete_director := await self.repository.delete(director_id=director_id)
        ):
            raise ValueError("Director not found")
        return delete_director
