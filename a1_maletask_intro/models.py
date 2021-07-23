from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'maletask_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # We need a list for every participant with 20 elements which contain random numbers from 1 to 20. These
        # determine which questions are shown. Each question will have its own page, so to be precise, the random
        # numbers determine, which pages will be shown in the second app.
        for p in self.get_players():
            p.participant.vars['quest_list'] = random.sample(range(1, 21), k=20)
            p.participant.vars['list_empty'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    testq = models.IntegerField()
