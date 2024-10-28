get_roles = {
    200: {
        "description": "Roles list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"role_id": 1, "role_name": "aaa"},
                    {"role_id": 2, "role_name": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Roles not found",
        "content": {
            "application/json": {
                "example": {"detail": "Roles not found"}
            }
        }
    }
}

get_role = {
    200: {
        "description": "Role fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "role_id": 1,
                    "role_name": "aaa"
                }
            }
        }
    },
    400: {
        "description": "Role not found",
        "content": {
            "application/json": {
                "example": {"detail": "Role not found"}
            }
        }
    }
}

create_role = {
    200: {
        "description": "Role create successfully",
        "content": {
            "application/json": {
                "example": {
                    "role_id": 1,
                    "role_name": "aaa"
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

update_role = {
    200: {
        "description": "Role update successfully",
        "content": {
            "application/json": {
                "example": {
                    "role_id": 1,
                    "rolename": "aaa",
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

delete_role = {
    200: {
        "description": "Role deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Role deleted successfully"}
            }
        }
    },
    400: {
        "description": "Role not found",
        "content": {
            "application/json": {
                "example": {"detail": "Role not found"}
            }
        }
    }
}
