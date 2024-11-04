get_content_languages = {
    200: {
        "description": "Content languages list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_language_id": 1, "content_id": 1, "language_id": 1},
                    {"content_language_id": 2, "content_id": 1, "language_id": 2},
                ]
            }
        },
    },
    400: {
        "description": "Content languages not found",
        "content": {
            "application/json": {"example": {"detail": "Content languages not found"}}
        },
    },
}

get_content_language = {
    200: {
        "description": "Content language fetched successfully",
        "content": {
            "application/json": {
                "example": {"content_language_id": 1, "content_id": 1, "language_id": 1}
            }
        },
    },
    400: {
        "description": "Content language not found",
        "content": {
            "application/json": {"example": {"detail": "Content language not found"}}
        },
    },
}

create_content_language = {
    200: {
        "description": "Content language create successfully",
        "content": {
            "application/json": {
                "example": {"content_language_id": 1, "content_id": 1, "language_id": 1}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_content_language = {
    200: {
        "description": "Content language update successfully",
        "content": {
            "application/json": {
                "example": {"content_language_id": 1, "content_id": 1, "language_id": 2}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_content_language = {
    200: {
        "description": "Content language deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content language deleted successfully"}
            }
        },
    },
    400: {
        "description": "Content language not found",
        "content": {
            "application/json": {"example": {"detail": "Content language not found"}}
        },
    },
}
