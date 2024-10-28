get_user_roles = {
    200: {
        "description": "User roles list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"user_role_id": 1, "user_id": 1, "role_id": 1},
                    {"user_role_id": 2, "user_id": 2, "role_id": 2}
                ]
            }
        }
    },
    400: {
        "description": "User roles not found",
        "content": {
            "application/json": {
                "example": {"detail": "User roles not found"}
            }
        }
    }
}

get_user_role = {
    200: {
        "description": "User role fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_role_id": 1,
                    "user_id": 1,
                    "role_id": 1
                }
            }
        }
    },
    400: {
        "description": "User role not found",
        "content": {
            "application/json": {
                "example": {"detail": "User role not found"}
            }
        }
    }
}

create_user_role = {
    200: {
        "description": "User role create successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_role_id": 1,
                    "user_id": 1,
                    "role_id": 1
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

update_user_role = {
    200: {
        "description": "User role update successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_role_id": 1,
                    "user_id": 1,
                    "role_id": 2
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

delete_user_role = {
    200: {
        "description": "User role deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "User role deleted successfully"}
            }
        }
    },
    400: {
        "description": "User role not found",
        "content": {
            "application/json": {
                "example": {"detail": "User role not found"}
            }
        }
    }
}
