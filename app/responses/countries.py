get_countries = {
    200: {
        "description": "Countries list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"country_id": 1, "country_name": "aaa"},
                    {"country_id": 1, "country_name": "bbb"}
                ]
            }
        }
    },
    400: {
        "description": "Countries not found",
        "content": {
            "application/json": {
                "example": {"detail": "Countries not found"}
            }
        }
    }
}

get_country = {
    200: {
        "description": "Country fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "country_id": 1, 
                    "country_name": "aaa"
                }
            }
        }
    },
    400: {
        "description": "Country not found",
        "content": {
            "application/json": {
                "example": {"detail": "Country not found"}
            }
        }
    }
}

create_country = {
    200: {
        "description": "Country create successfully",
        "content": {
            "application/json": {
                "example": {
                    "country_id": 1, 
                    "country_name": "aaa"
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

update_country = {
    200: {
        "description": "Country update successfully",
        "content": {
            "application/json": {
                "example": {
                    "country_id": 1, 
                    "country_name": "bbb"
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

delete_country = {
    200: {
        "description": "Country deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Country deleted successfully"}
            }
        }
    },
    400: {
        "description": "Country not found",
        "content": {
            "application/json": {
                "example": {"detail": "Country not found"}
            }
        }
    }
}