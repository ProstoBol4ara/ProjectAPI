get_content_genres = {
    200: {
        "description": "Content genres list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_genre_id": 1, "content_id": 1, "genre_id": 1},
                    {"content_genre_id": 2, "content_id": 1, "genre_id": 2}
                ]
            }
        }
    },
    400: {
        "description": "Content genres not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content genres not found"}
            }
        }
    }
}

get_content_genre = {
    200: {
        "description": "Content genre fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_genre_id": 1, 
                    "content_id": 1, 
                    "genre_id": 1
                }
            }
        }
    },
    400: {
        "description": "Content genre not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content genre not found"}
            }
        }
    }
}

create_content_genre = {
    200: {
        "description": "Content genre create successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_genre_id": 1, 
                    "content_id": 1, 
                    "genre_id": 1
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

update_content_genre = {
    200: {
        "description": "Content genre update successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_genre_id": 1, 
                    "content_id": 1, 
                    "genre_id": 2
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

delete_content_genre = {
    200: {
        "description": "Content genre deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content genre deleted successfully"}
            }
        }
    },
    400: {
        "description": "Content genre not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content genre not found"}
            }
        }
    }
}