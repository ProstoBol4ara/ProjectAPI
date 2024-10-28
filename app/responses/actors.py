get_actors = {
    200: {
        "description": "Actors list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"actor_id": 1, "actor_name": "aaa", "biography": "aaa", "birth_date": "2002-10-10"},
                    {"actor_id": 2, "actor_name": "bbb", "biography": "bbb", "birth_date": "2022-10-10"}
                ]
            }
        }
    },
    400: {
        "description": "Actors not found",
        "content": {
            "application/json": {
                "example": {"detail": "Actors not found"}
            }
        }
    }
}

get_actor = {
    200: {
        "description": "Actor fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "actor_id": 1,
                    "actor_name": "aaa",
                    "biography": "aaa",
                    "birth_date": "2002-10-10"
                }
            }
        }
    },
    400: {
        "description": "Actor not found",
        "content": {
            "application/json": {
                "example": {"detail": "Actor not found"}
            }
        }
    }
}

create_actor = {
    200: {
        "description": "Actor create successfully",
        "content": {
            "application/json": {
                "example": {
                    "actor_id": 1,
                    "actor_name": "aaa",
                    "biography": "aaa",
                    "birth_date": "10.10.1999"
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

update_actor = {
    200: {
        "description": "Actor update successfully",
        "content": {
            "application/json": {
                "example": {
                    "actor_id": 1,
                    "actor_name": "bbb",
                    "biography": "bbb"
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

delete_actor = {
    200: {
        "description": "Actor deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Actor deleted successfully"}
            }
        }
    },
    400: {
        "description": "Actor not found",
        "content": {
            "application/json": {
                "example": {"detail": "Actor not found"}
            }
        }
    }
}
