get_content_actors = {
    200: {
        "description": "Content actors list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_actor_id": 1, "content_id": 1, "actor_id": 1, "role": "Loser"},
                    {"content_actor_id": 1, "content_id": 1, "actor_id": 2, "role": "Niko-Niko-Nii"}
                ]
            }
        }
    },
    400: {
        "description": "Content actors not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content actors not found"}
            }
        }
    }
}

get_content_actor = {
    200: {
        "description": "Content actors fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_actor_id": 1,
                    "content_id": 1,
                    "actor_id": 1,
                    "role": "Loser"
                }
            }
        }
    },
    400: {
        "description": "Content actors not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content actors not found"}
            }
        }
    }
}

create_content_actor = {
    200: {
        "description": "Content actors create successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_actor_id": 1,
                    "content_id": 1,
                    "actor_id": 1,
                    "role": "Loser"
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

update_content_actor = {
    200: {
        "description": "Content actors update successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_actor_id": 1,
                    "content_id": 1,
                    "actor_id": 1,
                    "role": "Human"
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

delete_content_actor = {
    200: {
        "description": "Content actors deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content actors deleted successfully"}
            }
        }
    },
    400: {
        "description": "Content actors not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content actors not found"}
            }
        }
    }
}
