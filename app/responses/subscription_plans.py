get_subscription_plans = {
    200: {
        "description": "Subscription Plans list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"plan_id": 1, "plan_name": "aaa", "plan_price": 100},
                    {"plan_id": 2, "plan_name": "bbb", "plan_price": 200}
                ]
            }
        }
    },
    400: {
        "description": "Subscription Plans not found",
        "content": {
            "application/json": {
                "example": {"detail": "Subscription Plans not found"}
            }
        }
    }
}

get_subscription_plan = {
    200: {
        "description": "Subscription Plan fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "plan_id": 1, 
                    "plan_name": "aaa", 
                    "plan_price": 100
                }
            }
        }
    },
    400: {
        "description": "Subscription Plan not found",
        "content": {
            "application/json": {
                "example": {"detail": "Subscription Plan not found"}
            }
        }
    }
}

create_subscription_plan = {
    200: {
        "description": "Subscription Plan create successfully",
        "content": {
            "application/json": {
                "example": {
                    "plan_id": 1, 
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

update_subscription_plan = {
    200: {
        "description": "Subscription Plan update successfully",
        "content": {
            "application/json": {
                "example": {
                    "plan_id": 1, 
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

delete_subscription_plan = {
    200: {
        "description": "Subscription Plan deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Subscription Plan deleted successfully"}
            }
        }
    },
    400: {
        "description": "Subscription Plan not found",
        "content": {
            "application/json": {
                "example": {"detail": "Subscription Plan not found"}
            }
        }
    }
}