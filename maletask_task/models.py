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
    name_in_url = 'maletask_task'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rand_quest = models.IntegerField()
    next_rand_quest = models.IntegerField()

    # Variables for the questions:
    ar1 = models.IntegerField()
    ar2 = models.IntegerField()
    ar3 = models.IntegerField()
    ar4 = models.IntegerField()
    ar5 = models.IntegerField()

    ao1 = models.IntegerField()
    ao2 = models.IntegerField()
    ao3 = models.IntegerField()
    ao4 = models.IntegerField()
    ao5 = models.IntegerField()

    gs1 = models.IntegerField()
    gs2 = models.IntegerField()
    gs3 = models.IntegerField()
    gs4 = models.IntegerField()
    gs5 = models.IntegerField()

    mk1 = models.IntegerField()
    mk2 = models.IntegerField()
    mk3 = models.IntegerField()
    mk4 = models.IntegerField()
    mk5 = models.IntegerField()

    mc1 = models.IntegerField()
    mc2 = models.IntegerField()
    mc3 = models.IntegerField()
    mc4 = models.IntegerField()
    mc5 = models.IntegerField()
