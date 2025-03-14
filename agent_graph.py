from agent_tools import search_tool
from agent_schema import AgentSchema

from langgraph.graph import StateGraph, START, END

bot_workflow = StateGraph(AgentSchema)

bot_workflow.add_node("SearchAgent", search_tool.SearchAgent)
bot_workflow.add_node("ProblemSolvingAgent", search_tool.ProblemSolvingAgent)
bot_workflow.add_node("GetSearchRoute", search_tool.GetSearchRoute)
bot_workflow.add_node("GetWeather", search_tool.GetWeather)

bot_workflow.add_conditional_edges(
    "GetSearchRoute",
    search_tool.NodeCondition,
    {
        "news": "SearchAgent",
        "definitions": "SearchAgent",
        "weather": "GetWeather",
        "stocks": "SearchAgent",
        "maths": "ProblemSolvingAgent"
    }
)

bot_workflow.add_edge(START, "GetSearchRoute")
bot_workflow.add_edge("SearchAgent", END) 
bot_workflow.add_edge("GetWeather", END) 
bot_workflow.add_edge("ProblemSolvingAgent", END)

research_assistant = bot_workflow.compile()