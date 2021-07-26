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
    name_in_url = 'tr3_decisions'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    id1 = models.StringField()
    id2 = models.StringField()

    performance1 = models.IntegerField()
    performance2 = models.IntegerField()

    female_1 = models.IntegerField()
    female_2 = models.IntegerField()

    x = models.IntegerField()
    y = models.IntegerField()

    obs_num1 = models.IntegerField()
    obs_num2 = models.IntegerField()

    right_choice = models.IntegerField()

    chose_1 = models.IntegerField()
    chose_2 = models.IntegerField()

    equal_performance = models.IntegerField(
        initial=0
    )

    roundcount = models.IntegerField()

