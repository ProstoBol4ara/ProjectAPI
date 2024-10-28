get_directors = {
    200: {
        "description": "Directors list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"director_id": 1, "director_name": "aaa", "biography": "aaa", "birth_date": "2000-10-10"},
                    {"director_id": 2, "director_name": "bbb", "biography": "bbb", "birth_date": "2000-11-11"}
                ]
            }
        }
    },
    400: {
        "description": "Directors not found",
        "content": {
            "application/json": {
                "example": {"detail": "Directors not found"}
            }
        }
    }
}

get_director = {
    200: {
        "description": "Director fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "director_id": 1, 
                    "director_name": "aaa", 
                    "biography": "aaa", 
                    "birth_date": "2000-10-10"
                }
            }
        }
    },
    400: {
        "description": "Director not found",
        "content": {
            "application/json": {
                "example": {"detail": "Director not found"}
            }
        }
    }
}

create_director = {
    200: {
        "description": "Director create successfully",
        "content": {
            "application/json": {
                "example": {
                    "director_id": 1, 
                    "director_name": "aaa", 
                    "biography": "aaa", 
                    "birth_date": "2000-10-10"
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

update_director = {
    200: {
        "description": "Director update successfully",
        "content": {
            "application/json": {
                "example": {
                    "director_id": 1, 
                    "director_name": "bbb"
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

delete_director = {
    200: {
        "description": "Director deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Director deleted successfully"}
            }
        }
    },
    400: {
        "description": "Director not found",
        "content": {
            "application/json": {
                "example": {"detail": "Director not found"}
            }
        }
    }
}