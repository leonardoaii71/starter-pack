from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
from collections import namedtuple
from rasa_core import utils, constants
from rasa_core.agent import Agent
from rasa_core.channels.telegram import TelegramInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.run import serve_application, load_agent
from rasa_core.interpreter import (
    NaturalLanguageInterpreter)
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def train_dialogue(domain_file="domain.yml",
                   model_path="models/current/dialogue",
                   training_data_file="data/stories.md"):
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                              core_threshold=0.3,
                              nlu_threshold=0.1)

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2),
                            KerasPolicy(), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        epochs=300,
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
    model_directory = trainer.persist('models',
                                      fixed_model_name="nlu", project_name='current')

    return model_directory


def run(serve_forever=True):
    AvailableEndpoints = namedtuple('AvailableEndpoints', 'nlg '
                                                          'nlu '
                                                          'action '
                                                          'model')

    _endpoints = EndpointConfig(url="http://localhost:5055/webhook")
    try:
        _interpreter = RasaNLUInterpreter("models/current/nlu/")
        # load your trained agent
        agent = Agent.load("models/current/dialogue",
                           interpreter=_interpreter, action_endpoint=_endpoints)

        input_channel = TelegramInput(
            # you get this when setting up a bot
            access_token="516790963:AAEgzLnFfhmNk48eEwqb1sfFD-HqAThQHT4",
            # this is your bots username
            verify="regispucmm_bot",
            # the url your bot should listen for messages
            webhook_url="https://www.sysservices.site/webhooks/telegram/webhook"
        )

        # set serve_forever=False if you want to keep the server running
        s = agent.handle_channels([input_channel], 5005, serve_forever=False)

    except:
        raise Exception("Failed to run")


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
    elif task == "train-nlu":
        train_nlu()
    elif task == "run":
        run()
