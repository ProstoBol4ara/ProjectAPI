get_user_subscriptions = {
    200: {
        "description": "User subscriptions list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"user_subscription_id": 1, "plan_name": "aaa", "plan_price": 100},
                    {"user_subscription_id": 2, "plan_name": "bbb", "plan_price": 200}
                ]
            }
        }
    },
    400: {
        "description": "User subscriptions not found",
        "content": {
            "application/json": {
                "example": {"detail": "User subscriptions not found"}
            }
        }
    }
}

get_user_subscription = {
    200: {
        "description": "User subscription fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_subscription_id": 1, 
                    "plan_name": "aaa", 
                    "plan_price": 100
                }
            }
        }
    },
    400: {
        "description": "User subscription not found",
        "content": {
            "application/json": {
                "example": {"detail": "User subscription not found"}
            }
        }
    }
}

create_user_subscription = {
    200: {
        "description": "User subscription create successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_subscription_id": 1, 
                    "plan_name": "aaa", 
                    "plan_price": 100
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

update_user_subscription = {
    200: {
        "description": "User subscription update successfully",
        "content": {
            "application/json": {
                "example": {
                    "user_subscription_id": 1, 
                    "plan_name": "bbb", 
                    "plan_price": 100
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

delete_user_subscription = {
    200: {
        "description": "User subscription deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "User subscription deleted successfully"}
            }
        }
    },
    400: {
        "description": "User subscription not found",
        "content": {
            "application/json": {
                "example": {"detail": "User subscription not found"}
            }
        }
    }
}