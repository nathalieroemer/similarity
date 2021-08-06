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
    name_in_url = 'a3_maletask_quest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Written promotion:
    promotion = models.LongStringField()

    # Promotion, other questons:
    promo6scale = models.IntegerField()
    promo100scale = models.IntegerField()

    # Beliefs about correctly answered questions
    belief_correct_q = models.IntegerField()

    # Questionnaire:

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
