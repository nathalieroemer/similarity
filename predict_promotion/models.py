import pandas as pd
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
import itertools
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'predict_promo'
    players_per_group = None
    num_rounds = 252
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("supporter.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['word', 'photoid', 'promo_txt', 'female', 'recog', 'orig50', 'image_data'])
    index = df.index
    number_of_rows = len(index)
    df_shuffled = df.sample(frac=1).reset_index()

    words = df_shuffled['word'].to_list()
    promo = df_shuffled['promo_txt'].to_list()
    photo_ids = df_shuffled['photoid'].to_list()
    female = df_shuffled['female'].to_list()
    recog = df_shuffled['recog'].to_list()
    orig = df_shuffled['orig50'].to_list()
    index_old = df_shuffled['index'].to_list()
    image_data = df_shuffled['image_data'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['words'] = Constants.df['word'].to_list()
        self.session.vars['photo_id'] = Constants.df['photoid'].to_list()
        self.session.vars['image_data'] = Constants.df['image_data'].to_list()
        self.session.vars['promo'] = Constants.df['promo_txt'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()
        self.session.vars['recog'] = Constants.df['recog'].to_list()
        self.session.vars['orig'] = Constants.df['orig50'].to_list()

        for p in self.get_players():
           # if p.participant.id_in_session <= 39:
                l = list(range(0,252))
                random.shuffle(l)
                p.participant.vars['list'] = l

            #    p.participant.vars['list'] = range(0, 49)
            #elif 11 >= p.participant.id_in_session <= 20:
            #    l = list(range(50, 99))
            #    random.shuffle(l)
            #    p.participant.vars['list'] = l
            #elif 21 >= p.participant.id_in_session <= 30:
            #    l = list(range(100, 149))
           #     random.shuffle(l)
            #    p.participant.vars['list'] = l
            #elif 21 >= p.participant.id_in_session <= 30:
            #    l  = list(range(150, 199))
           #     random.shuffle(l)
           #     p.participant.vars['list'] = l
            #elif 31 >= p.participant.id_in_session <= 40:
            #    l = list(range(200, 249))
            #    random.shuffle(l)
             #   p.participant.vars['list'] = l

                p.participant.vars['passed_instr'] = 0
                p.participant.vars['list_is_empty'] = 0
                p.participant.vars['end'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    roundcount = models.IntegerField()
    photoid = models.StringField()
    word = models.StringField()
    promo=models.StringField()

    fem_pay = models.CurrencyField()
    orig_pay = models.CurrencyField()
    recog_pay = models.CurrencyField()

    guess_gender = models.IntegerField()
    guess_orig = models.IntegerField()
    guess_recog = models.IntegerField()
    dev_recog = models.FloatField()

    orig = models.IntegerField()
    recog = models.FloatField()
    female = models.IntegerField()

    payoffround = models.IntegerField()



    x = models.IntegerField()
    photo_id = models.StringField()