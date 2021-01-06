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
    data = pd.read_csv("picdata.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['player.image_data', 'player.word', 'player.photoid', 'player.promo_verbal', 'player.promo_rec', 'player.promo_orig', 'orig', 'recog', 'value'])
    index = df.index
    number_of_rows = len(index)

    image_data = df['player.image_data'].to_list()
    words = df['player.word'].to_list()
    photo_ids = df['player.photoid'].to_list()
    promo_verbal = df['player.promo_verbal'].to_list()
    promo_rec = df['player.promo_rec'].to_list()
    promo_orig = df['player.promo_orig'].to_list()
    orig = df['orig'].to_list()
    recog = df['recog'].to_list()
    value = df['value'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle(['verbal_only', 'score_only', 'verbal_idea', 'score_idea', 'idea_only'])
        self.session.vars['image_data'] = Constants.df['player.image_data'].to_list()
        self.session.vars['words'] = Constants.df['player.word'].to_list()
        self.session.vars['photo_id'] = Constants.df['player.photoid'].to_list()
        self.session.vars['promo_rec'] = Constants.df['player.promo_rec'].to_list()
        self.session.vars['promo_verbal'] = Constants.df['player.promo_verbal'].to_list()
        self.session.vars['promo_orig'] = Constants.df['player.promo_orig'].to_list()
        self.session.vars['orig'] = Constants.df['orig'].to_list()
        self.session.vars['recog'] = Constants.df['recog'].to_list()
        self.session.vars['value'] = Constants.df['value'].to_list()

        for p in self.get_players():
            p.treat = next(treat)
            p.participant.vars['treat'] = p.treat
            p.participant.vars['list'] = random.sample(range(Constants.number_of_rows), k=20)
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

    testq = models.IntegerField(
        label="What determines the value of an illustration?",
        choices=[
            [1, 'Its aesthetic value and the number of objects used'],
            [2, 'Its originality and its recognizability'],
            [3, 'The number of objects used and its originality'],
            [4, 'The length of the illustrated word and its recognizability'],
        ],
        widget=widgets.RadioSelect
    )

  #  def custom_export(players):
  #      yield ['session', 'participant_code', 'round_number', 'id_in_group', 'payoff', 'photoid']
  #      for p in players:
  #          yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.payoff, p.participant.vars.get('photoid', None)]
