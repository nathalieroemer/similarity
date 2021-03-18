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
    name_in_url = 'a1_intro_task'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("investor.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['playerimage_data', 'word', 'photo_id', 'playerpromo_verbal', 'female', 'value', 'recog', 'originality50'])
    index = df.index
    number_of_rows = len(index)

    image_data = df['playerimage_data'].to_list()
    words = df['word'].to_list()
    photo_ids = df['photo_id'].to_list()
    promo_verbal = df['playerpromo_verbal'].to_list()
    orig = df['originality50'].to_list()
    recog = df['recog'].to_list()
    value = df['value'].to_list()
    female = df['female'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle(['verbal_only', 'verbal_idea', 'idea_only', 'verbal_only_b', 'verbal_idea_b', 'idea_only_b'])
        self.session.vars['image_data'] = Constants.df['playerimage_data'].to_list()
        self.session.vars['words'] = Constants.df['word'].to_list()
        self.session.vars['photo_id'] = Constants.df['photo_id'].to_list()
        self.session.vars['promo_verbal'] = Constants.df['playerpromo_verbal'].to_list()
        self.session.vars['orig'] = Constants.df['originality50'].to_list()
        self.session.vars['recog'] = Constants.df['recog'].to_list()
        self.session.vars['value'] = Constants.df['value'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()

        for p in self.get_players():
            p.treat = next(treat)
            p.participant.vars['treat'] = p.treat
            # hier wird für jeden Teilnehmer eine zufällige Liste gezogen mit Zahlen die den Zeilen der Liste entsprechen
            p.participant.vars['list'] = random.sample(range(Constants.number_of_rows), k=34)
            p.participant.vars['list_is_empty'] = 0
            p.participant.vars['passed_quest'] = 0

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
