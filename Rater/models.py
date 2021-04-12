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
    name_in_url = 'a1_intro_task'
    players_per_group = None
    num_rounds = 24
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("add_rater.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['playerimage_data', 'playerword', 'playerphotoid'])
    index = df.index
    number_of_rows = len(index)
    df_shuffled = df.sample(frac=1).reset_index()

    image_data = df_shuffled['playerimage_data'].to_list()
    words = df_shuffled['playerword'].to_list()
    photo_ids = df_shuffled['playerphotoid'].to_list()
    index_old = df_shuffled['index'].to_list()
    print(index_old)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['image_data'] = Constants.df['playerimage_data'].to_list()
        self.session.vars['words'] = Constants.df['playerword'].to_list()
        self.session.vars['photo_id'] = Constants.df['playerphotoid'].to_list()
        # print(self.session.vars['count_obs'])

        for p in self.get_players():
           # if p.participant.id_in_session <= 39:
                l = list(range(0,24))
                # print(l)
                random.shuffle(l)
                p.participant.vars['list'] = l
                p.participant.vars['count_round'] = 0
                p.participant.vars['no_ideas_left'] = 0
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
    photoid = models.StringField()
    word = models.StringField()
    word_guess = models.StringField(
        blank=True
    )
    x = models.IntegerField()
    photo_id = models.StringField()
    no_left = models.IntegerField()
