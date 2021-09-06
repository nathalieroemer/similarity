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
    name_in_url = 'p2'
    players_per_group = None
    num_rounds = 3  # TODO: has to be adjusted


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    x = models.IntegerField()
    promo = models.StringField()

    score = models.IntegerField()
    female = models.IntegerField()

    g_score = models.IntegerField()
    g_fem = models.IntegerField()

    dev_score = models.IntegerField()
    score_pay = models.CurrencyField()
    gen_pay = models.CurrencyField()
