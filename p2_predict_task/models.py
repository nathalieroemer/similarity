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
    name_in_url = 'p2_predict_task'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    x = models.IntegerField()
    promo = models.StringField()

    answers = models.IntegerField()
    female = models.IntegerField()
    # TODO: Hilfsvariable kann entfernt werden, wenn mit neuem Datensatz gelöst.
    hilfe = models.IntegerField()

    g_answers = models.IntegerField()
    g_fem = models.IntegerField()

    dev_ans = models.IntegerField()
    ans_pay = models.CurrencyField()
    gen_pay = models.CurrencyField()
