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
    # Variables for the questions:
    rand_quest = models.IntegerField()
    next_rand_quest = models.IntegerField()
    answer = models.IntegerField()
    right = models.IntegerField()

    # Part 2:
    promotion = models.LongStringField()

    # Part 3:
    performance = models.IntegerField()
    perf_slider = models.IntegerField()
    application = models.IntegerField()
    success = models.IntegerField()

    # Questionnaire:
    colorb = models.IntegerField()
    native = models.IntegerField()
    eng_prof = models.IntegerField(
        blank=True  # Only shown if not native
    )
    difficult = models.IntegerField()
    stereotypes = models.IntegerField()
    bonus_chance = models.IntegerField()
    prom_quality = models.IntegerField()
    risk_pref = models.IntegerField()
    competition = models.IntegerField()
