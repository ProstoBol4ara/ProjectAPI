get_users = {
    200: {
        "description": "Users list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"user_id": 1, "username": "aaa"},
                    {"user_id": 2, "username": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Users not found",
        "content": {
            "application/json": {
                "example": {"detail": "Users not found"}
            }
        }
    }
}

get_user = {
    200: {
        "description": "User fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_id": 1, 
                    "username": "aaa"
                }
            }
        }
    },
    400: {
        "description": "User not found",
        "content": {
            "application/json": {
                "example": {"detail": "User not found"}
            }
        }
    }
}

create_user = {
    200: {
        "description": "User create successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_id": 1, 
                    "username": "aaa",
                    "email": "aaa@aaa.com"
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

update_user = {
    200: {
        "description": "User update successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_id": 1, 
                    "username": "aaa",
                    "email": "aaa@aaa.com"
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

delete_user = {
    200: {
        "description": "User deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "User deleted successfully"}
            }
        }
    },
    400: {
        "description": "User not found",
        "content": {
            "application/json": {
                "example": {"detail": "User not found"}
            }
        }
    }
}