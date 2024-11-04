get_favorites = {
    200: {
        "description": "Favorites list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"favorite_id": 1, "user_id": 1, "content_id": 1},
                    {"favorite_id": 2, "user_id": 1, "content_id": 2},
                ]
            }
        },
    },
    400: {
        "description": "Favorites not found",
        "content": {"application/json": {"example": {"detail": "Favorites not found"}}},
    },
}

get_favorite = {
    200: {
        "description": "Favorite fetched successfully",
        "content": {
            "application/json": {
                "example": {"favorite_id": 1, "user_id": 1, "content_id": 1}
            }
        },
    },
    400: {
        "description": "Favorite not found",
        "content": {"application/json": {"example": {"detail": "Favorite not found"}}},
    },
}

create_favorite = {
    200: {
        "description": "Favorite create successfully",
        "content": {
            "application/json": {
                "example": {"favorite_id": 1, "user_id": 1, "content_id": 1}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_favorite = {
    200: {
        "description": "Favorite update successfully",
        "content": {
            "application/json": {
                "example": {
                    "favorite_id": 1,
                    "user_id": 2,
                }
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_favorite = {
    200: {
        "description": "Favorite deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Favorite deleted successfully"}
            }
        },
    },
    400: {
        "description": "Favorite not found",
        "content": {"application/json": {"example": {"detail": "Favorite not found"}}},
    },
}
