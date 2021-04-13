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
    name_in_url = 'baseminar_2_invest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    word_1 = models.StringField()
    word_2 = models.StringField()

    value_1 = models.IntegerField()
    value_2 = models.IntegerField()

    photo_id_1 = models.StringField()
    photo_id_2 = models.StringField()

  #  photo_verbal_1 = models.LongStringField()
 #   photo_verbal_2 = models.LongStringField()

    female_1 = models.IntegerField()
    female_2 = models.IntegerField()

    x = models.IntegerField()
    y = models.IntegerField()

    obs_num1 = models.IntegerField()
    obs_num2 = models.IntegerField()

    right_choice = models.IntegerField()

    list = models.LongStringField()
    chose_1 = models.IntegerField()
    chose_2 = models.IntegerField()

    equal_value = models.IntegerField(
        initial=0
    )

    roundcount = models.IntegerField()

    gender = models.IntegerField()
    name = models.StringField()
    pay_euro = models.IntegerField()