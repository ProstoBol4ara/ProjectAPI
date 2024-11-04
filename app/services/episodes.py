from repositories import EpisodesRepository
from constants import date_pattern
from re import match


class EpisodesService:
    def __init__(self, repository: EpisodesRepository):
        self.repository = repository

    async def get_all(self):
        episodes = await self.repository.get_all()

        return (
            None
            if episodes is None
            else [
                {
                    "episode_id": episode.episode_id,
                    "content_id": episode.content_id,
                    "season_number": episode.season_number,
                    "episode_number": episode.episode_number,
                    "title": episode.title,
                    "release_date": episode.release_date,
                    "episode_path": episode.episode_path,
                }
                for episode in episodes
            ]
        )

    async def get_one(self, episode_id: int):
        if not episode_id:
            raise ValueError("episode_id cannot be empty")

        episode = await self.repository.get_one(episode_id=episode_id)

        if not episode:
            raise ValueError("Episode not found")

        return {
            "episode_id": episode.episode_id,
            "content_id": episode.content_id,
            "season_number": episode.season_number,
            "episode_number": episode.episode_number,
            "title": episode.title,
            "release_date": episode.release_date,
            "episode_path": episode.episode_path,
        }

    async def create(
        self,
        content_id: int,
        season_number: int = None,
        episode_number: int = None,
        title: str = None,
        release_date: str = None,
        episode_path: str = None,
    ):

        if not content_id:
            raise ValueError("content_id cannot be empty")

        if not release_date or not match(date_pattern, release_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        new_episode = await self.repository.create(
            content_id=content_id,
            season_number=season_number,
            episode_number=episode_number,
            title=title,
            release_date=release_date,
            episode_path=episode_path,
        )

        return {
            "episode_id": new_episode.episode_id,
            "content_id": new_episode.content_id,
            "season_number": new_episode.season_number,
            "episode_number": new_episode.episode_number,
            "title": new_episode.title,
            "release_date": new_episode.release_date,
            "episode_path": new_episode.episode_path,
        }

    async def update(
        self,
        episode_id: int,
        content_id: int = None,
        season_number: int = None,
        episode_number: int = None,
        title: str = None,
        release_date: str = None,
        episode_path: str = None,
    ):

        if not episode_id:
            raise ValueError("episode_id cannot be empty")

        if not release_date or not match(date_pattern, release_date):
            raise ValueError("Invalid birth_date! Date format: day.month.year")

        episode = await self.repository.update(
            episode_id=episode_id,
            content_id=content_id,
            season_number=season_number,
            episode_number=episode_number,
            title=title,
            release_date=release_date,
            episode_path=episode_path,
        )

        if not episode:
            raise ValueError("Episode not found")

        return {
            "episode_id": episode.episode_id,
            "content_id": episode.content_id,
            "season_number": episode.season_number,
            "episode_number": episode.episode_number,
            "title": episode.title,
            "release_date": episode.release_date,
            "episode_path": episode.episode_path,
        }

    async def delete(self, episode_id: int):
        if not episode_id:
            raise ValueError("episode_id cannot be empty")

        if not (delete_episode := await self.repository.delete(episode_id=episode_id)):
            raise ValueError("Episode not found")
        return delete_episode
