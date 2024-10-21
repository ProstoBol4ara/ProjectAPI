from repositories import EpisodesRepository

class EpisodesService:
    def __init__(self, episodes_repository: EpisodesRepository):
        self.episodes_repository = episodes_repository

    async def get_episodes(self):
        return await self.episodes_repository.get_episode()

    async def get_episode(self, episode_id: int):
        return await self.episodes_repository.get_episode(episode_id=episode_id)

    async def create_episode(self, content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        return await self.episodes_repository.create_episode(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)

    async def update_episode(self, episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        return await self.episodes_repository.update_episode(episode_id=episode_id, content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)

    async def delete_episode(self, episode_id: int):
        await self.episodes_repository.delete_episode(episode_id=episode_id)
    