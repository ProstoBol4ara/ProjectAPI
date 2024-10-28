get_payment_methods = {
    200: {
        "description": "Payment methods list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"payment_method_id": 1, "user_id": 1, "method_type": "aaa"},
                    {"payment_method_id": 2, "user_id": 1, "method_type": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Payment methods not found",
        "content": {
            "application/json": {
                "example": {"detail": "Payment methods not found"}
            }
        }
    }
}

get_payment_method = {
    200: {
        "description": "Payment method fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_method_id": 1, 
                    "user_id": 1, 
                    "method_type": "aaa"
                }
            }
        }
    },
    400: {
        "description": "Payment method not found",
        "content": {
            "application/json": {
                "example": {"detail": "Payment method not found"}
            }
        }
    }
}

create_payment_method = {
    200: {
        "description": "Payment method create successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_method_id": 1, 
                    "user_id": 1, 
                    "method_type": "aaa", 
                    "provider": "aaa", 
                    "account_number": "XXXXX-XXXXX-XXXXX-XXXXX"
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

update_payment_method = {
    200: {
        "description": "Payment method update successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_method_id": 2, 
                    "user_id": 1, 
                    "method_type": "bbb"
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

delete_payment_method = {
    200: {
        "description": "Payment method deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Payment method deleted successfully"}
            }
        }
    },
    400: {
        "description": "Payment method not found",
        "content": {
            "application/json": {
                "example": {"detail": "Payment method not found"}
            }
        }
    }
}