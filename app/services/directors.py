from repositories import DirectorsRepository

class DirectorsService:
    def __init__(self, directors_repository: DirectorsRepository):
        self.directors_repository = directors_repository

    async def get_directors(self):
        return await self.directors_repository.get_directors()

    async def get_director(self, director_id: int):
        return await self.directors_repository.get_director(director_id=director_id)

    async def create_director(self, director_name: str, biography: str = None, birth_date: str = None):
        return await self.directors_repository.create_director(director_name=director_name, biography=biography, birth_date=birth_date)

    async def update_director(self, director_id: int, director_name: str = None, biography:str = None, birth_date: str = None):
        return await self.directors_repository.update_director(director_id=director_id, director_name=director_name, biography=biography, birth_date=birth_date)

    async def delete_director(self, director_id: int):
        await self.directors_repository.delete_director(director_id=director_id)
    