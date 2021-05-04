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
    name_in_url = 'tr7_intro_task'
    players_per_group = None
    num_rounds = 1
    IMAGE_EXTENTION = 'png'
    data = pd.read_csv("supporter_upload_s38.csv", delimiter=",", encoding="latin1")
    df = pd.DataFrame(data, columns=['image_data', 'word', 'photoid', 'promo_txt', 'female', 'value', 'recog', 'orig50', 'count_obs_pb', 'count_obs_ib', 'count_obs_pib', 'count_obs_p', 'count_obs_i', 'count_obs_fi', 'count_obs_ni'])
    index = df.index
    number_of_rows = len(index)

    image_data = df['image_data'].to_list()
    words = df['word'].to_list()
    photo_ids = df['photoid'].to_list()
    promo_verbal = df['promo_txt'].to_list()
    orig = df['orig50'].to_list()
    recog = df['recog'].to_list()
    value = df['value'].to_list()
    female = df['female'].to_list()
    count_obs_pb = df['count_obs_pb'].to_list()
    count_obs_ib = df['count_obs_ib'].to_list()
    count_obs_pib = df['count_obs_pib'].to_list()
    count_obs_p = df['count_obs_p'].to_list()
    count_obs_i = df['count_obs_i'].to_list()
    count_obs_fi = df['count_obs_fi'].to_list()
    count_obs_ni = df['count_obs_ni'].to_list()


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle(['verbal_only', 'verbal_idea', 'idea_only', 'verbal_only_b', 'verbal_idea_b', 'idea_only_b', 'no_info'])
        self.session.vars['image_data'] = Constants.df['image_data'].to_list()
        self.session.vars['words'] = Constants.df['word'].to_list()
        self.session.vars['photo_id'] = Constants.df['photoid'].to_list()
        self.session.vars['promo_verbal'] = Constants.df['promo_txt'].to_list()
        self.session.vars['orig'] = Constants.df['orig50'].to_list()
        self.session.vars['recog'] = Constants.df['recog'].to_list()
        self.session.vars['value'] = Constants.df['value'].to_list()
        self.session.vars['female'] = Constants.df['female'].to_list()

        # capturing obs per idea in treatment promotion blind
        self.session.vars['count_obs_pb'] = Constants.df['count_obs_pb'].to_list()

        # capturing obs per idea in treatment idea blind
        self.session.vars['count_obs_ib'] = Constants.df['count_obs_ib'].to_list()

        # capturing obs per idea in treatment promotion & idea blind
        self.session.vars['count_obs_pib'] = Constants.df['count_obs_pib'].to_list()

        # capturing obs per idea in treatment promotion revealed
        self.session.vars['count_obs_p'] = Constants.df['count_obs_p'].to_list()
        print("count obs list", self.session.vars['count_obs_p'])
        # capturing obs per idea in treatment idea revealed
        self.session.vars['count_obs_i'] = Constants.df['count_obs_i'].to_list()

        # capturing obs per idea in treatment full info
        self.session.vars['count_obs_fi'] = Constants.df['count_obs_fi'].to_list()

        # capturing obs per idea in no info
        self.session.vars['count_obs_ni'] = Constants.df['count_obs_ni'].to_list()


        for p in self.get_players():
            p.treat = next(treat)
            p.participant.vars['treat'] = p.treat
            # hier wird für jeden Teilnehmer eine zufällige Liste gezogen mit Zahlen die den Zeilen der Liste entsprechen
            p.participant.vars['list'] = list(range(0,252))
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
