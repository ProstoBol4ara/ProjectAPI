get_payments = {
    200: {
        "description": "Payments list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"payment_id": 1, "pay_per_view_id": 1, "payment_method_id": 1},
                    {"payment_id": 2, "pay_per_view_id": 2, "payment_method_id": 2},
                ]
            }
        },
    },
    400: {
        "description": "Payments not found",
        "content": {"application/json": {"example": {"detail": "Payments not found"}}},
    },
}

get_payment = {
    200: {
        "description": "Payment fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_id": 1,
                    "pay_per_view_id": 1,
                    "payment_method_id": 1,
                }
            }
        },
    },
    400: {
        "description": "Payment not found",
        "content": {"application/json": {"example": {"detail": "Payment not found"}}},
    },
}

create_payment = {
    200: {
        "description": "Payment create successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_id": 1,
                    "pay_per_view_id": 1,
                    "payment_method_id": 1,
                }
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_payment = {
    200: {
        "description": "Payment update successfully",
        "content": {
            "application/json": {
                "example": {
                    "payment_id": 1,
                    "pay_per_view_id": 1,
                    "payment_method_id": 2,
                }
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_payment = {
    200: {
        "description": "Payment deleted successfully",
        "content": {
            "application/json": {"example": {"message": "Payment deleted successfully"}}
        },
    },
    400: {
        "description": "Payment not found",
        "content": {"application/json": {"example": {"detail": "Payment not found"}}},
    },
}
