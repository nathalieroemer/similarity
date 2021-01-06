from django.contrib.staticfiles.templatetags.staticfiles import static
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import io
import os
import re
import base64
from PIL import Image
from django.conf import settings
from os import path
from uuid import uuid4
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from random import seed
from random import randint


class Welcome(Page):
    from_model='player'


class Instructions(Page):
    form_model = 'player'


class Test(Page):
    form_model = 'player'
    form_fields = ['testq']

page_sequence = [Welcome, Instructions, Test]
