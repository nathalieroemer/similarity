import os
from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, '_static')
MEDIA_URL = '_static/'

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.30, doc="",
    mturk_hit_settings=dict(
    keywords='bonus, study',
    title='Task',
    description='Depending on your performance, you can earn up to $1.80 in 5 minutes in this task.',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=20,
    expiration_hours=2 * 24,
    qualification_requirements=[
        {
        'QualificationTypeId': "00000000000000000071",
       'Comparator': "In",
        'LocaleValues': [{'Country': "US"}, {'Country': "GB"}, {'Country': "CA"}, {'Country': "AU"}, {'Country': "IN"}]
        },
        {
        'QualificationTypeId': "38ASA1XP59Y2SB4QW6YC4OOEET8GHV", # to prevent retakes
        'Comparator': "DoesNotExist",
        },
        ],
        grant_qualification_id="38ASA1XP59Y2SB4QW6YC4OOEET8GHV", # to prevent retakes
        ),
)

SESSION_CONFIGS = [
    dict(
        name='maletask_intro',  ## name muss app name entsprechen
        display_name='maletask_intro',  ### display name kann gleich sein
        num_demo_participants=50,
        app_sequence=['a1_maletask_intro', 'a2_maletask_test', 'a3_maletask_quest'],
        ## hier kann ich auch weitere apps hinzufügen, namen entsprechen ordner namen
    ),
    dict(
        name='tr3_1_intro_task',
        display_name='Employer male typed task',
        num_demo_participants=50,
        app_sequence=['tr3_1_intro_task', 'tr3_2_investment'],
        ## hier kann ich auch weitere apps hinzufügen, namen entsprechen ordner namen
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '(r)%s)(c+6*zp7utwg8mw@9$*muwn^fh3&!id%&wgid5r7!^=i'

INSTALLED_APPS = ['otree']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
