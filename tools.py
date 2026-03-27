from langchain_core.tools import tool
from typing import List, Optional
from models import UserPreference, MovieRecommendation
from db import get_store

@tool
def save_user_preference(mood: str, avoid_elements: List[str]) -> UserPreference:
    """사용자의 현재 상태와 기피 요소를 저장합니다."""
    pref = UserPreference(mood=mood, avoid_elements=avoid_elements)
    store = get_store()
    store["user_preference"].append(pref)
    return pref

@tool
def record_recommendation(title: str, year: int, logline: str) -> str:
    """추천된 영화를 DB에 기록합니다."""
    store = get_store()
    store["recommended_movies"].append({"title": title, "year": year, "logline": logline})
    return f"영화 '{title}' 추천 기록 완료"

@tool
def get_history() -> str:
    """사용자의 이전 취향과 추천 이력을 조회합니다."""
    store = get_store()
    pref = store["user_preference"][-1] if store["user_preference"] else "기록 없음"
    movies = [m["title"] for m in store["recommended_movies"][-5:]] # 최근 5건
    return f"최근 기분: {pref}\n최근 추천 목록: {', '.join(movies)}"
