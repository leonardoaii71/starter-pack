from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from rasa_core import utils
from rasa_core.agent import Agent
# from rasa_core.channels.console import
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def train_dialogue(domain_file="domain.yml",
                   model_path="models/current/dialogue",
                   training_data_file="data/stories.md"):

    fallback = FallbackPolicy(fallback_action_name="utter_default",
                              core_threshold=0.3,
                              nlu_threshold=0.3)

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2),
                            KerasPolicy(), fallback],)

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/nlu_data.md')
    trainer = Trainer(config.load("nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/current/',
                                      fixed_model_name="nlu")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/current/nlu/")
    agent = Agent.load("models/current/dialogue", interpreter=interpreter)
    if serve_forever:
        #agent.handle_channel(ConsoleInputChannel())
        return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
