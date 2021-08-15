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
    name_in_url = 'p1_predict_intro'
    players_per_group = None
    num_rounds = 1
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
        # The variables are saved as session.vars to access and manipulate them later in the experiment.
        self.session.vars['words'] = Constants.df['word'].to_list()
        self.session.vars['photo_id'] = Constants.df['photoid'].to_list()
        self.session.vars['image_data'] = Constants.df['image_data'].to_list()
        self.session.vars['promo'] = Constants.df['promo_txt'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()
        self.session.vars['recog'] = Constants.df['recog'].to_list()
        self.session.vars['orig'] = Constants.df['orig50'].to_list()

        for p in self.get_players():
            # Every player gets a list assigned with shuffled numbers between 0 and 252 via which the data sets are
            # identified later in the experiment.
            li = list(range(0, 252))
            random.shuffle(li)
            p.participant.vars['list'] = li

            p.participant.vars['list_is_empty'] = 0
            p.participant.vars['end'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    test = models.IntegerField()
