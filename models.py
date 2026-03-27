from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class UserPreference(BaseModel):
    mood: str = Field(description="사용자의 현재 기분 또는 상황")
    avoid_elements: List[str] = Field(description="절대 보기 싫은 요소 (지뢰)")
    preferred_genres: Optional[List[str]] = Field(description="선호하는 장르")

class MovieRecommendation(BaseModel):
    title: str = Field(description="영화 제목")
    year: int = Field(description="개봉 연도")
    reason: str = Field(description="추천 사유 (사용자 기분과의 매칭)")
    safety_check: str = Field(description="지뢰 요소가 없는 이유 설명")
    logline: str = Field(description="한 줄 줄거리")
    snack_recommendation: str = Field(description="어울리는 간식")
