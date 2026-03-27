_store: dict = {
    "user_preference": [], # 사용자의 기분, 기피 요소
    "recommended_movies": [], # AI가 추천한 영화 이력
    "watchlist": [], # 사용자가 찜한 영화
}

def get_store():
    return _store
