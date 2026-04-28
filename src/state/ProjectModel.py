from pydantic import BaseModel, Field
from typing import List, Dict



class Project(BaseModel):
    start_prompt: str
    project_plan: List[str] = Field(default_factory=list) # Здесь список задач TODO
    project_state: Dict[str, str] = Field(default_factory=dict) # Здесь мапа: "название задачи" -> "статус (например, todo/done)"
    review_state: str = Field(default_factory='') #здесь мы будем хранить вердикт ревьюшки
    is_ready: bool = False
