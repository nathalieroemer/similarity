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
    name_in_url = 'InvestorDecisions'
    players_per_group = None
    num_rounds = 15


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    word_1 = models.StringField()
    word_2 = models.StringField()

    value_1 = models.IntegerField()
    value_2 = models.IntegerField()

    orig_1 = models.IntegerField()
    orig_2 = models.IntegerField()

    recog_1 = models.IntegerField()
    recog_2 = models.IntegerField()

    photo_id_1 = models.StringField()
    photo_id_2 = models.StringField()

    photo_verbal_1 = models.LongStringField()
    photo_verbal_2 = models.LongStringField()

    promo_rec_1 = models.IntegerField()
    promo_rec_2 = models.IntegerField()

    promo_orig_1 = models.IntegerField()
    promo_orig_2 = models.IntegerField()

    x = models.IntegerField()
    y = models.IntegerField()

    right_choice = models.IntegerField()

    list = models.LongStringField()
    chose_1 = models.StringField()
    chose_2 = models.StringField()

#    gender = models.IntegerField()
    english = models.IntegerField()
    english_prof = models.IntegerField(
        blank=True
    )
    colourb = models.IntegerField()
    stereotypes = models.IntegerField()
    chance_bonus = models.IntegerField()
    risk_pref = models.IntegerField()
    comp = models.IntegerField()
