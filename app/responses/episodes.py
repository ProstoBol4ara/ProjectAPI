get_episodes = {
    200: {
        "description": "Episodes list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"episode_id": 1, "content_id": 1, "season_number": 1, "episode_number": 1, "title": "aaa", "release_date": "2000-10-10", "episode_path": "/ep1"},
                    {"episode_id": 2, "content_id": 1, "season_number": 1, "episode_number": 2, "title": "bbb", "release_date": "2000-11-11", "episode_path": "/ep2"}
                ]
            }
        }
    },
    400: {
        "description": "Episodes not found",
        "content": {
            "application/json": {
                "example": {"detail": "Episodes not found"}
            }
        }
    }
}

get_episode = {
    200: {
        "description": "Episode fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "episode_id": 1,
                    "content_id": 1,
                    "season_number": 1,
                    "episode_number": 1,
                    "title": "aaa",
                    "release_date": "2000-10-10",
                    "episode_path": "/ep1"
                }
            }
        }
    },
    400: {
        "description": "Episode not found",
        "content": {
            "application/json": {
                "example": {"detail": "Episode not found"}
            }
        }
    }
}

create_episode = {
    200: {
        "description": "Episode create successfully",
        "content": {
            "application/json": {
                "example": {
                    "episode_id": 1,
                    "content_id": 1,
                    "season_number": 1,
                    "episode_number": 1,
                    "title": "aaa",
                    "release_date": "2000-10-10",
                    "episode_path": "/ep1"
                }
            }
        }
    },
    400: {
        "description": "Any problem",
        "content": {
            "application/json": {
                "example": {"detail": "..."}
            }
        }
    }
}

update_episode = {
    200: {
        "description": "Episode update successfully",
        "content": {
            "application/json": {
                "example": {
                    "episode_id": 1,
                    "title": "bbb"
                }
            }
        }
    },
    400: {
        "description": "Any problem",
        "content": {
            "application/json": {
                "example": {"detail": "..."}
            }
        }
    }
}

delete_episode = {
    200: {
        "description": "Episode deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Episode deleted successfully"}
            }
        }
    },
    400: {
        "description": "Episode not found",
        "content": {
            "application/json": {
                "example": {"detail": "Episode not found"}
            }
        }
    }
}
