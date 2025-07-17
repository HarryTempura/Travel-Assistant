from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.types import Command

from common.commands import THINK
from entity.plan_state import PlanState
from nodes.question import question_node, question_cond
from nodes.understanding import understanding_node


def get_agent():
    agent_builder = StateGraph(PlanState)

    agent_builder.add_node('question', question_node, )
    agent_builder.add_node('understanding', understanding_node)

    agent_builder.set_entry_point('question')

    agent_builder.add_conditional_edges('question', question_cond)

    return agent_builder.compile()


def planning_node(state=None):
    agent = get_agent()

    command = Command(update={'location': state['location']})
    config = RunnableConfig(configurable={'thread_id': 1}, recursion_limit=150)

    events = agent.stream(command, config, stream_mode='values')
    for event in events:
        message = event.get('messages')
        if isinstance(message, AIMessage):
            response = message[-1].content
            if THINK in response:
                response = response.split(THINK, 1)[-1].strip()
                message[-1].content = response
