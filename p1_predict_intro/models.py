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
    name_in_url = 'p1'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("supporter_test.csv", delimiter=";", encoding="latin1")
    df = pd.DataFrame(data, columns=['participantcode', 'promo_txt', 'female', 'score'])
    index = df.index
    number_of_rows = len(index)
    df_shuffled = df.sample(frac=1).reset_index()

    p_id = df_shuffled['participantcode'].to_list()
    promo = df_shuffled['promo_txt'].to_list()
    female = df_shuffled['female'].to_list()
    score = df_shuffled['score'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        # The variables are saved as session.vars to access and manipulate them later in the experiment.
        self.session.vars['p_ids'] = Constants.df['participantcode'].to_list()
        self.session.vars['promo'] = Constants.df['promo_txt'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()
        self.session.vars['score'] = Constants.df['score'].to_list()

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
