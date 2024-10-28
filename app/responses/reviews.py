get_reviews = {
    200: {
        "description": "Reviews list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"review_id": 1, "content_id": 1, "user_id": 1, "rating": 1, "comment": "aaa"},
                    {"review_id": 2, "content_id": 1, "user_id": 2, "rating": 4, "comment": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Reviews not found",
        "content": {
            "application/json": {
                "example": {"detail": "Reviews not found"}
            }
        }
    }
}

get_review = {
    200: {
        "description": "Review fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "review_id": 1,
                    "content_id": 1,
                    "user_id": 1,
                    "rating": 1,
                    "comment": "aaa"
                }
            }
        }
    },
    400: {
        "description": "Review not found",
        "content": {
            "application/json": {
                "example": {"detail": "Review not found"}
            }
        }
    }
}

create_review = {
    200: {
        "description": "Review create successfully",
        "content": {
            "application/json": {
                "example": {
                    "review_id": 1,
                    "content_id": 1,
                    "user_id": 1,
                    "rating": 1,
                    "comment": "aaa"
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

update_review = {
    200: {
        "description": "Review update successfully",
        "content": {
            "application/json": {
                "example": {
                    "review_id": 1,
                    "content_id": 1,
                    "user_id": 1,
                    "rating": 5,
                    "comment": "aaa"
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

delete_review = {
    200: {
        "description": "Review deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Review deleted successfully"}
            }
        }
    },
    400: {
        "description": "Review not found",
        "content": {
            "application/json": {
                "example": {"detail": "Review not found"}
            }
        }
    }
}
