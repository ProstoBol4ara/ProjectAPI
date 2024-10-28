get_languages = {
    200: {
        "description": "Languages list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"language_id": 1, "name": "aaa"},
                    {"language_id": 2, "name": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Languages not found",
        "content": {
            "application/json": {
                "example": {"detail": "Languages not found"}
            }
        }
    }
}

get_language = {
    200: {
        "description": "Language fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "language_id": 1, 
                    "name": "aaa"
                }
            }
        }
    },
    400: {
        "description": "Language not found",
        "content": {
            "application/json": {
                "example": {"detail": "Language not found"}
            }
        }
    }
}

create_language = {
    200: {
        "description": "Language create successfully",
        "content": {
            "application/json": {
                "example": {
                    "language_id": 1, 
                    "name": "aaa"
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

update_language = {
    200: {
        "description": "Language update successfully",
        "content": {
            "application/json": {
                "example": {
                    "language_id": 1, 
                    "name": "bbb"
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

delete_language = {
    200: {
        "description": "Language deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Language deleted successfully"}
            }
        }
    },
    400: {
        "description": "Language not found",
        "content": {
            "application/json": {
                "example": {"detail": "Language not found"}
            }
        }
    }
}