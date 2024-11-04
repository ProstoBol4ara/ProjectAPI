get_pay_per_views = {
    200: {
        "description": "Pay per views list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"pay_per_view_id": 1, "amount": 100, "content_id": 1},
                    {"pay_per_view_id": 2, "amount": 200, "content_id": 2},
                ]
            }
        },
    },
    400: {
        "description": "Pay per views not found",
        "content": {
            "application/json": {"example": {"detail": "Pay per views not found"}}
        },
    },
}

get_pay_per_view = {
    200: {
        "description": "Pay per view fetched successfully",
        "content": {
            "application/json": {
                "example": {"pay_per_view_id": 1, "amount": 100, "content_id": 1}
            }
        },
    },
    400: {
        "description": "Pay per view not found",
        "content": {
            "application/json": {"example": {"detail": "Pay per view not found"}}
        },
    },
}

create_pay_per_view = {
    200: {
        "description": "Pay per view create successfully",
        "content": {
            "application/json": {
                "example": {"pay_per_view_id": 1, "amount": 100, "content_id": 1}
            }
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

update_pay_per_view = {
    200: {
        "description": "Pay per view update successfully",
        "content": {
            "application/json": {"example": {"pay_per_view_id": 1, "amount": 200}}
        },
    },
    400: {
        "description": "Any problem",
        "content": {"application/json": {"example": {"detail": "..."}}},
    },
}

delete_pay_per_view = {
    200: {
        "description": "Pay per view deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Pay per view deleted successfully"}
            }
        },
    },
    400: {
        "description": "Pay per view not found",
        "content": {
            "application/json": {"example": {"detail": "Pay per view not found"}}
        },
    },
}
