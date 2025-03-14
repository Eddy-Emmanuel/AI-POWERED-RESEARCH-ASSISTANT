from pydantic import BaseModel, Field
from typing import TypedDict, Literal

class AgentSchema(TypedDict):
    input_message:str
    search_result:str
    query_route:str
    
class AgentSearchRoute(BaseModel):
    search_route : Literal["news", "definitions", "weather", "stocks", "maths"] = Field(..., description="This specifies the category of information the agent should retrieve, such as news updates, word definitions, weather forecasts, stock market data, or shopping results.")