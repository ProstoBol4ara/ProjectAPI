get_content_countries = {
    200: {
        "description": "Сontent countries list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_country_id": 1, "content_id": 1, "country_id": 1},
                    {"content_country_id": 2, "content_id": 2, "country_id": 1},
                ]
            }
        },
    },
    400: {
        "description": "Сontent countries not found",
        "content": {
            "application/json": {"example": {"detail": "Сontent countries not found"}}
        },
    },
}

get_content_country = {
    200: {
        "description": "Content country fetched successfully",
        "content": {
            "application/json": {
                "example": {"content_country_id": 1, "content_id": 1, "country_id": 1}
            }
        },
    },
    400: {
        "description": "Content country not found",
        "content": {
            "application/json": {"example": {"detail": "Content country not found"}}
        },
    },
}

create_content_country = {
    200: {
        "description": "Content country create successfully",
        "content": {
            "application/json": {
                "example": {"content_country_id": 1, "content_id": 1, "country_id": 1}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_content_country = {
    200: {
        "description": "Content country update successfully",
        "content": {
            "application/json": {
                "example": {"content_country_id": 1, "content_id": 1, "country_id": 2}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_content_country = {
    200: {
        "description": "Content country deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content country deleted successfully"}
            }
        },
    },
    400: {
        "description": "Content country not found",
        "content": {
            "application/json": {"example": {"detail": "Content country not found"}}
        },
    },
}
