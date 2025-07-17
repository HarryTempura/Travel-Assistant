from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from common.commands import THINK
from common.llms import OLLAMA_QWEN3_06B


def understanding_node(state):
    """
    根据用户提供的问题和答案，生成用户对本次旅行的期望。

    :param state: 包含用户问题和答案的字典
    :return: 包含用户旅行期望的字典
    """
    # 定义系统模板，指导AI如何处理用户信息
    sys_template = """
### 指令

根据用户给出的信息用最短的语句总结出用户对于本次旅行的期望之一。

### 注意！只输出一句话！避免任何额外的输出！
    """.strip()
    # 创建系统消息模板
    sys_message = SystemMessagePromptTemplate.from_template(sys_template)
    # 定义人类模板，包含用户问题和答案，引导AI生成旅行期望
    human_template = f"""
问题：{state['question']}

回答：{state['answer']}

期望：
    """.strip()
    # 创建人类消息模板
    human_message = HumanMessagePromptTemplate.from_template(human_template)
    # 创建聊天提示模板，结合系统和人类消息模板
    prompt = ChatPromptTemplate.from_messages([sys_message, human_message])

    # 创建处理链，连接提示模板和AI模型，并设置输出解析器
    chain = prompt | OLLAMA_QWEN3_06B | StrOutputParser()

    # 调用链生成响应
    response = chain.invoke({})

    # 如果响应包含特定关键字，移除关键字及其之前的内容
    if THINK in response:
        response = response.split(THINK, 1)[-1].strip()

    return {'request': [response]}
