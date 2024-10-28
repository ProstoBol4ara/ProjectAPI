get_contents = {
    200: {
        "description": "Contents list fetched successfully",
        "content": {
            "application/json": {
                "example": [
                    {"content_id": 1, "title": "aaa", "preview_path": "/preview1.jpg", "description": "aaa", "release_date": "2002-10-11", "content_type": "Movie", "content_path": "/1"},
                    {"content_id": 2, "title": "bbb", "preview_path": "/preview1.jpg", "description": "bbb", "release_date": "2002-10-10", "content_type": "Serial", "content_path": "/2"}
                ]
            }
        }
    },
    400: {
        "description": "Contents not found",
        "content": {
            "application/json": {
                "example": {"detail": "Contents not found"}
            }
        }
    }
}

get_content = {
    200: {
        "description": "Content fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_id": 1, 
                    "title": "aaa", 
                    "preview_path": "/preview1.jpg", 
                    "description": "aaa", 
                    "release_date": "2002-10-11", 
                    "content_type": "Movie", 
                    "content_path": "/1"
                }
            }
        }
    },
    400: {
        "description": "Content not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content not found"}
            }
        }
    }
}

create_content = {
    200: {
        "description": "Content create successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_id": 1, 
                    "title": "aaa", 
                    "preview_path": "/preview1.jpg", 
                    "description": "aaa", 
                    "release_date": "2002-10-11", 
                    "content_type": "Movie", 
                    "content_path": "/1"
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

update_content = {
    200: {
        "description": "Content update successfully",
        "content": {
            "application/json": {
                "example": {
                    "content_id": 1, 
                    "title": "aaa", 
                    "preview_path": "/preview1.jpg", 
                    "description": "bbb", 
                    "release_date": "2002-10-11", 
                    "content_type": "Movie", 
                    "content_path": "/1"
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

delete_content = {
    200: {
        "description": "Content deleted successfully",
        "content": {
            "application/json": {
                "example": {"message": "Content deleted successfully"}
            }
        }
    },
    400: {
        "description": "Content not found",
        "content": {
            "application/json": {
                "example": {"detail": "Content not found"}
            }
        }
    }
}