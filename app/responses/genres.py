get_genres = {
    200: {
        "description": "Genres list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"genre_id": 1, "genre_name": "aaa"},
                    {"genre_id": 2, "genre_name": "bbb"},
                ]
            }
        },
    },
    400: {
        "description": "Genres not found",
        "content": {"application/json": {"example": {"detail": "Genres not found"}}},
    },
}

get_genre = {
    200: {
        "description": "Genre fetched successfully",
        "content": {
            "application/json": {"example": {"genre_id": 1, "genre_name": "aaa"}}
        },
    },
    400: {
        "description": "Genre not found",
        "content": {"application/json": {"example": {"detail": "Genre not found"}}},
    },
}

create_genre = {
    200: {
        "description": "Genre create successfully",
        "content": {
            "application/json": {"example": {"genre_id": 1, "genre_name": "aaa"}}
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_genre = {
    200: {
        "description": "Genre update successfully",
        "content": {
            "application/json": {"example": {"genre_id": 1, "genre_name": "bbb"}}
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_genre = {
    200: {
        "description": "Genre deleted successfully",
        "content": {
            "application/json": {"example": {"message": "Genre deleted successfully"}}
        },
    },
    400: {
        "description": "Genre not found",
        "content": {"application/json": {"example": {"detail": "Genre not found"}}},
    },
}
