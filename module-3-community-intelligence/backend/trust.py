def calculate_trust(likes: int, dislikes: int) -> str:
    if likes >= dislikes + 3:
        return "TRUSTED"
    elif dislikes >= likes + 3:
        return "FAKE / UNVERIFIED"
    else:
        return "NEEDS CONFIRMATION"
