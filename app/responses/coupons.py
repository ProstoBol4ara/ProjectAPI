get_coupons = {
    200: {
        "description": "Coupons list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"coupon_id": 1, "code": "aaa", "discount_percentage": "0.05", "valid_from": "2000-10-10", "valid_until": "2000-11-11"},
                    {"coupon_id": 2, "code": "bbb", "discount_percentage": "0.01", "valid_from": "2000-11-11", "valid_until": "2000-12-12"}
                ]
            }
        }
    },
    400: {
        "description": "Coupons not found",
        "content": {
            "application/json": {
                "example": {"detail": "Coupons not found"}
            }
        }
    }
}

get_coupon = {
    200: {
        "description": "Coupon fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "coupon_id": 1,
                    "code": "aaa",
                    "discount_percentage": "0.05",
                    "valid_from": "2000-10-10",
                    "valid_until": "2000-11-11"
                }
            }
        }
    },
    400: {
        "description": "Coupon not found",
        "content": {
            "application/json": {
                "example": {"detail": "Coupon not found"}
            }
        }
    }
}

create_coupon = {
    200: {
        "description": "Coupon create successfully",
        "content": {
            "application/json": {
                "example": {
                    "coupon_id": 1,
                    "code": "aaa",
                    "discount_percentage": "0.05",
                    "valid_from": "2000-10-10",
                    "valid_until": "2000-11-11"
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

update_coupon = {
    200: {
        "description": "Coupon update successfully",
        "content": {
            "application/json": {
                "example": {
                    "coupon_id": 1,
                    "code": "bbb",
                    "discount_percentage": "0.05",
                    "valid_from": "2000-10-10",
                    "valid_until": "2000-11-11"
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

delete_coupon = {
    200: {
        "description": "Coupon deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Coupon deleted successfully"}
            }
        }
    },
    400: {
        "description": "Coupon not found",
        "content": {
            "application/json": {
                "example": {"detail": "Coupon not found"}
            }
        }
    }
}
