from repositories import EpisodesRepository

class EpisodesService:
    def __init__(self, episodes_repository: EpisodesRepository):
        self.episodes_repository = episodes_repository

    async def get_episodes(self):
        episodes = await self.episodes_repository.get_episode()
        return None if episodes is None else [{"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path} for episode in episodes]

    async def get_episode(self, episode_id: int):
        episode = await self.episodes_repository.get_episode(episode_id=episode_id)
        return None if episode is None else {"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path}

    async def create_episode(self, content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        new_episode = await self.episodes_repository.create_episode(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        return {"episode_id": new_episode.episode_id, "content_id": new_episode.content_id, "season_number": new_episode.season_number, "episode_number": new_episode.episode_number, "title": new_episode.title, "release_date": new_episode.release_date, "episode_path": new_episode.episode_path}

    async def update_episode(self, episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        episode = await self.episodes_repository.update_episode(episode_id=episode_id, content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        return None if episode is None else {"episode_id": episode.episode_id, "content_id": episode.content_id, "season_number": episode.season_number, "episode_number": episode.episode_number, "title": episode.title, "release_date": episode.release_date, "episode_path": episode.episode_path}

    async def delete_episode(self, episode_id: int):
        return await self.episodes_repository.delete_episode(episode_id=episode_id)
    