from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.types import Command

from entity.plan_state import PlanState
from nodes.question import question_node


def get_agent():
    agent_builder = StateGraph(PlanState)

    agent_builder.add_node(question_node)

    agent_builder.set_entry_point('question_node')

    return agent_builder.compile()


def planning_node(state=None):
    agent = get_agent()

    command = Command(update={'location': state['location']})
    config = RunnableConfig(configurable={'thread_id': 1}, recursion_limit=150)

    events = agent.stream(command, config, stream_mode='values')
    for event in events:
        pass
