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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'a1_maletask_test'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for the questions:
    rand_quest = models.IntegerField()
    next_rand_quest = models.IntegerField()
    answer = models.IntegerField()
    right = models.IntegerField()
    timeout = models.IntegerField()