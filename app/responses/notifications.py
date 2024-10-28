get_notifications = {
    200: {
        "description": "Notifications list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"notification_id": 1, "message": "aaa", "user_id": 1},
                    {"notification_id": 2, "message": "bbb", "user_id": 1}
                ]
            }
        }
    },
    400: {
        "description": "Notifications not found",
        "content": {
            "application/json": {
                "example": {"detail": "Notifications not found"}
            }
        }
    }
}

get_notification = {
    200: {
        "description": "Notification fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "notification_id": 1, 
                    "message": "aaa", 
                    "user_id": 1
                }
            }
        }
    },
    400: {
        "description": "Notification not found",
        "content": {
            "application/json": {
                "example": {"detail": "Notification not found"}
            }
        }
    }
}

create_notification = {
    200: {
        "description": "Notification create successfully",
        "content": {
            "application/json": {
                "example": {
                    "notification_id": 1, 
                    "message": "aaa", 
                    "user_id": 1
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

update_notification = {
    200: {
        "description": "Notification update successfully",
        "content": {
            "application/json": {
                "example": {
                    "notification_id": 1, 
                    "message": "bbb"
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

delete_notification = {
    200: {
        "description": "Notification deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Notification deleted successfully"}
            }
        }
    },
    400: {
        "description": "Notification not found",
        "content": {
            "application/json": {
                "example": {"detail": "Notification not found"}
            }
        }
    }
}