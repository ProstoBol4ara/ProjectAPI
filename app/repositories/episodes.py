from database import AsyncSession
from models import Episodes

class EpisodesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_episodes(self):
        episodes = await self.db.execute(select(Episodes))
        return episodes.scalar().all()

    async def get_episode(self, episode_id: int):
        episode = await self.db.execute(
            select(Episodes).where(Episodes.episode_id == episode_id)
        )
        return episode.scalar_one_or_none()

    async def create_episode(self, content_id: int, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        if not release_date is None:
            release_date = datetime.strptime(release_date, '%d.%m.%Y').date()
        new_episode = Episodes(content_id=content_id, season_number=season_number, episode_number=episode_number, title=title, release_date=release_date, episode_path=episode_path)
        self.db.add(new_episode)
        await self.db.commit()
        await self.db.refresh(new_episode)
        return new_episode

    async def update_episode(self, episode_id: int, content_id: int = None, season_number: int = None, episode_number: int = None, title: str = None, release_date: str = None, episode_path: str = None):
        episode = await self.db.execute(
            select(Episodes).where(Episodes.episode_id == episode_id)
        )
        episode = episode.scalar_one_or_none()

        if title:
            episode.title = title
        if content_id:
            episode.content_id = content_id
        if release_date:
            episode.release_date = datetime.strptime(release_date, '%d.%m.%Y').date()
        if episode_path:
            episode.episode_path = episode_path
        if season_number:
            episode.season_number = season_number
        if episode_number:
            episode.episode_number = episode_number

        await self.db.commit()
        await self.db.refresh(episode)
        return episode

    async def delete_episode(self, episode_id: int):
        await self.db.execute(
            delete(Episodes).where(Episodes.episode_id == episode_id)
        )
        await self.db.commit()