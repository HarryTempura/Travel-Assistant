from langchain_core.messages import SystemMessage, HumanMessage

from common.llms import OLLAMA_QWEN3_06B
from entity.questions import Questions


def question_node(state=None):
    """
    根据用户提供的目的地信息，生成并提出一系列问题以完善旅行计划细节。

    :param state: 包含用户已提供目的地信息的字典，默认为None。
    :return: 包含用户对旅行计划各项细节回答的字典。
    """
    # 初始化带有结构化输出的大型语言模型
    llm = OLLAMA_QWEN3_06B.with_structured_output(Questions)

    # 系统提示信息，定义了用户需求和专家角色
    sys_prompt = """
你是一名旅行规划专家。用户现在想做一个旅行规划，但是现在只明确了目的地，规划中很多信息还不明确。

### 指令

和用户明确旅行的主题（放松度假、文化探索等）、预算、必去景点、计划出行时间和地点、个人偏好等问题。给出问题列表。

### 注意！避免任何额外的输出！
    """.strip()

    # 根据用户提供的目的地构建人类提示信息
    human_prompt = f'我想去{state["location"]}玩。'

    # 使用大型语言模型生成具体问题列表
    questions = llm.invoke([SystemMessage(content=sys_prompt), HumanMessage(content=human_prompt)])
    questions = questions.question

    # 初始化字典以存储问题及其答案
    ques_answer = {}
    for question in questions:
        # 提出问题并接收用户输入的答案
        answer = input(f'Assistant:\n{question}')
        # 将问题和答案存储在字典中
        ques_answer[question] = answer

    # 返回包含所有问题答案的字典
    return {'ques_answer': ques_answer}
