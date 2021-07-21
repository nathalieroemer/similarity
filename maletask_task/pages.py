from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class AR1(Page):
    form_model = 'player'
    form_fields = [
        'ar1'
    ]

    def is_displayed(self):
        # In the first round, the random question is determined by the value of the participant variable, whose value
        # was assigned to it at the end of the previous app. A participant var had to be used to pass it between apps.
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        # In later rounds, the random question is determined by the value of "next_rand_quest" from the previous round,
        # which has a new value at the end of every round (see below).
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        # The page is displayed if the number for the random question is 1.
        return self.player.rand_quest == 1

    def before_next_page(self):
        # Before the next page, the next value from the question list (a participant var) is assigned to the variable
        # next_rand_quest, which will determine the value of the rand_quest in the next round.
        # We cannot just let this assignment happen in a is_displayed method, we have to use next_rand_quest, as this
        # determines, which page will be shown. is_displayed is only executed, when the next page is already shown.
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            # The element is deleted after it determines the next question:
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1

        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AR2(Page):
    form_model = 'player'
    form_fields = [
        'ar2'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 2

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AR3(Page):
    form_model = 'player'
    form_fields = [
        'ar3'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 3

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AR4(Page):
    form_model = 'player'
    form_fields = [
        'ar4'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 4

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AR5(Page):
    form_model = 'player'
    form_fields = [
        'ar5'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 5

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AO1(Page):
    form_model = 'player'
    form_fields = [
        'ao1'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 6

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects1="{}.png".format("objects1"),
        )

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AO2(Page):
    form_model = 'player'
    form_fields = [
        'ao2'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 7

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects2="{}.png".format("objects2"),
        )

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AO3(Page):
    form_model = 'player'
    form_fields = [
        'ao3'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 8

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects3="{}.png".format("objects3"),
        )

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AO4(Page):
    form_model = 'player'
    form_fields = [
        'ao4'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 9

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects4="{}.png".format("objects4"),
        )

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class AO5(Page):
    form_model = 'player'
    form_fields = [
        'ao5'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 10

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects5="{}.png".format("objects5"),
        )

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class GS1(Page):
    form_model = 'player'
    form_fields = [
        'gs1'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 11

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class GS2(Page):
    form_model = 'player'
    form_fields = [
        'gs2'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 12

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class GS3(Page):
    form_model = 'player'
    form_fields = [
        'gs3'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 13

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class GS4(Page):
    form_model = 'player'
    form_fields = [
        'gs4'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 14

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class GS5(Page):
    form_model = 'player'
    form_fields = [
        'gs5'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 15

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MK1(Page):
    form_model = 'player'
    form_fields = [
        'mk1'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 16

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MK2(Page):
    form_model = 'player'
    form_fields = [
        'mk2'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 17

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MK3(Page):
    form_model = 'player'
    form_fields = [
        'mk3'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 18

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MK4(Page):
    form_model = 'player'
    form_fields = [
        'mk4'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 19

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MK5(Page):
    form_model = 'player'
    form_fields = [
        'mk5'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 20

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MC1(Page):
    form_model = 'player'
    form_fields = [
        'mc1'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 21

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MC2(Page):
    form_model = 'player'
    form_fields = [
        'mc2'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 22

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MC3(Page):
    form_model = 'player'
    form_fields = [
        'mc3'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 23

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MC4(Page):
    form_model = 'player'
    form_fields = [
        'mc4'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 24

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class MC5(Page):
    form_model = 'player'
    form_fields = [
        'mc5'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 25

    def before_next_page(self):
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class Results(Page):
    def is_displayed(self):
        return self.round_number == 20


page_sequence = [
    AR1,
    AR2,
    AR3,
    AR4,
    AR5,
    AO1,
    AO2,
    AO3,
    AO4,
    AO5,
    GS1,
    GS2,
    GS3,
    GS4,
    GS5,
    MK1,
    MK2,
    MK3,
    MK4,
    MK5,
    MC1,
    MC2,
    MC3,
    MC4,
    MC5,
    Results]
