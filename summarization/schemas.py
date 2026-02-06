from pydantic import BaseModel, Field
from typing import List

class FinalSummary(BaseModel):
    title: str = Field(description="Punchy title")
    elevator_pitch: str = Field(description="2-sentence overview")
    key_insights: List[str] = Field(description="Bullet points of data/findings")
    next_steps: List[str] = Field(description="Action items for the reader")