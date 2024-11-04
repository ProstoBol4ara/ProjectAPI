get_content_directors = {
    200: {
        "description": "Content directors list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_director_id": 1, "content_id": 1, "director_id": 1},
                    {"content_director_id": 2, "content_id": 1, "director_id": 2},
                ]
            }
        },
    },
    400: {
        "description": "Content directors not found",
        "content": {
            "application/json": {"example": {"detail": "Content directors not found"}}
        },
    },
}

get_content_director = {
    200: {
        "description": "Content director fetched successfully",
        "content": {
            "application/json": {
                "example": {"content_director_id": 1, "content_id": 1, "director_id": 1}
            }
        },
    },
    400: {
        "description": "Content director not found",
        "content": {
            "application/json": {"example": {"detail": "Content director not found"}}
        },
    },
}

create_content_director = {
    200: {
        "description": "Content director create successfully",
        "content": {
            "application/json": {
                "example": {"content_director_id": 1, "content_id": 1, "director_id": 1}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_content_director = {
    200: {
        "description": "Content director update successfully",
        "content": {
            "application/json": {
                "example": {"content_director_id": 1, "content_id": 1, "director_id": 2}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_content_director = {
    200: {
        "description": "Content director deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content director deleted successfully"}
            }
        },
    },
    400: {
        "description": "Content director not found",
        "content": {
            "application/json": {"example": {"detail": "Content director not found"}}
        },
    },
}
