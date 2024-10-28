get_watch_historys = {
    200: {
        "description": "Watch historys list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"watch_history_id": 1, "user_id": 1, "content_id": 1},
                    {"watch_history_id": 2, "user_id": 1, "content_id": 2}
                ]
            }
        }
    },
    400: {
        "description": "Watch historys not found",
        "content": {
            "application/json": {
                "example": {"detail": "Watch historys not found"}
            }
        }
    }
}

get_watch_history = {
    200: {
        "description": "Watch history fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "watch_history_id": 1,
                    "user_id": 1,
                    "content_id": 1
                }
            }
        }
    },
    400: {
        "description": "Watch history not found",
        "content": {
            "application/json": {
                "example": {"detail": "Watch history not found"}
            }
        }
    }
}

create_watch_history = {
    200: {
        "description": "Watch history create successfully",
        "content": {
            "application/json": {
                "example": {
                    "watch_history_id": 1,
                    "user_id": 1,
                    "content_id": 1
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

update_watch_history = {
    200: {
        "description": "Watch history update successfully",
        "content": {
            "application/json": {
                "example": {
                    "watch_history_id": 1,
                    "user_id": 1,
                    "content_id": 2
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

delete_watch_history = {
    200: {
        "description": "Watch history deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Watch history deleted successfully"}
            }
        }
    },
    400: {
        "description": "Watch history not found",
        "content": {
            "application/json": {
                "example": {"detail": "Watch history not found"}
            }
        }
    }
}