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

import random
import itertools
import pandas as pd

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ra_1_intro_task'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("supporterdec_rest.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['playerimage_data', 'female', 'playerphotoid'])
    index = df.index
    number_of_rows = len(index)

    image_data = df['playerimage_data'].to_list()
    photo_ids = df['playerphotoid'].to_list()
    female = df['female'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle(['no_info', 'no_info'])
        self.session.vars['image_data'] = Constants.df['playerimage_data'].to_list()
        self.session.vars['photo_id'] = Constants.df['playerphotoid'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()
        print("female obs", self.session.vars['female'])


        for p in self.get_players():
            p.treat = next(treat)
            p.participant.vars['treat'] = p.treat
            # hier wird für jeden Teilnehmer eine zufällige Liste gezogen mit Zahlen die den Zeilen der Liste entsprechen
            p.participant.vars['list'] = list(range(0,68))
            random.shuffle(p.participant.vars['list'])
            p.participant.vars['list_is_empty'] = 0
            p.participant.vars['passed_quest'] = 0
            p.participant.vars['count_round'] = 1

    def custom_export(session):
        yield ['treat']
        for s in session:
            yield [s.treat]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.StringField()
    testq = models.IntegerField()

  #  def custom_export(players):
  #      yield ['session', 'participant_code', 'round_number', 'id_in_group', 'payoff', 'photoid']
  #      for p in players:
  #          yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.payoff, p.participant.vars.get('photoid', None)]