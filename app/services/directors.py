from repositories import DirectorsRepository

class DirectorsService:
    def __init__(self, directors_repository: DirectorsRepository):
        self.directors_repository = directors_repository

    async def get_directors(self):
        directors = await self.directors_repository.get_directors()
        return None if directors is None else \
            [{"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography,
              "birth_date": director.birth_date} for director in directors]

    async def get_director(self, director_id: int):
        director = await self.directors_repository.get_director(director_id=director_id)

        if not director: raise ValueError("Coupon not found")

        return {"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography,
                "birth_date": director.birth_date}

    async def create_director(self, director_name: str, biography: str = None, birth_date: str = None):
        new_director = await self.directors_repository\
            .create_director(director_name=director_name, biography=biography, birth_date=birth_date)
        return {"director_id": new_director.director_id, "director_name": new_director.director_name,
                "biography": new_director.biography, "birth_date": new_director.birth_date}

    async def update_director(self, director_id: int, director_name: str = None, biography:str = None, birth_date: str = None):
        director = await self.directors_repository\
            .update_director(director_id=director_id, director_name=director_name, biography=biography, birth_date=birth_date)

        if not director: raise ValueError("Director not found")

        return {"director_id": director.director_id, "director_name": director.director_name, "biography": director.biography,
                "birth_date": director.birth_date}

    async def delete_director(self, director_id: int):
        if not await self.directors_repository.delete_director(director_id=director_id):
            raise ValueError("Director not found")
