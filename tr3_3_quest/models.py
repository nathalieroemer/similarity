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
    name_in_url = 'tr3_3_quest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    gender = models.IntegerField()
    english = models.IntegerField()
    english_prof = models.IntegerField(
        blank=True
    )
    colourb = models.IntegerField(
        blank=True
    )
    stereotypes = models.IntegerField()
    chance_bonus = models.IntegerField()
    risk_pref = models.IntegerField()
    comp = models.IntegerField()
