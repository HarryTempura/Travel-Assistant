from dotenv import load_dotenv
from loguru import logger

from nodes.planning import planning_node

load_dotenv()


def start():
    location = input('输入目的地：\n')

    input_state = {'location': location}

    planning_node(input_state)


if __name__ == '__main__':
    logger.info('Start... ...')

    start()

    logger.info('End')
