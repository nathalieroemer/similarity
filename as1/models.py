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
    name_in_url = 'AS_Intro'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'jpg'
    data = pd.read_csv(
        "data_image_similarity_v2.csv",
        delimiter=";",
        encoding="latin1"
    )
    df = pd.DataFrame(
        data,
        columns=[
            'image_data1',
            'image_data2',
            'word',
            'treatment',
            'pin_code'
        ]
    )
    index = df.index
    number_of_rows = len(index)
    df_shuffled = df.sample(frac=1).reset_index()

    words = df_shuffled['word'].to_list()
    treatments = df_shuffled['treatment'].to_list()
    photo_ids = df_shuffled['pin_code'].to_list()
    image_data1 = df_shuffled['image_data1'].to_list()
    image_data2 = df_shuffled['image_data2'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['words'] = Constants.df_shuffled['word'].to_list()
        self.session.vars['treatments'] = Constants.df_shuffled['treatment'].to_list()
        self.session.vars['photo_ids'] = Constants.df_shuffled['pin_code'].to_list()
        self.session.vars['image_data1'] = Constants.df_shuffled['image_data1'].to_list()
        self.session.vars['image_data2'] = Constants.df_shuffled['image_data2'].to_list()

        for p in self.get_players():
            # l_ins = list(range(116))
            # l_base = list(range(122))
            # random.shuffle(l_ins)
            # random.shuffle(l_base)
            # del l_base[:6]

            # p.participant.vars['list_ins'] = l_ins
            # p.participant.vars['list_base'] = l_base
            # Liste mit 236 Werten von 0 bis 235.
            li = list(range(236))
            random.shuffle(li)
            p.participant.vars['list'] = li


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
