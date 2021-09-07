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

import pandas as pd
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'AS_Task'
    players_per_group = None
    num_rounds = 115


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    x = models.IntegerField()
    y = models.IntegerField()

    photo_id1 = models.StringField()
    photo_id2 = models.StringField()
    word1 = models.StringField()
    word2 = models.StringField()
    treatment1 = models.IntegerField()
    treatment2 = models.IntegerField()

    c_term = models.IntegerField()
    c_material = models.IntegerField()
    c_display = models.IntegerField()
    c_overall = models.IntegerField()
