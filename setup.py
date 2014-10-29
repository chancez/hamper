#!/usr/bin/env python2

from setuptools import setup, find_packages

from hamper import version

setup(
    name='hamper',
    version=version.encode('utf8'),
    description='Yet another IRC bot',
    author='Mike Cooper',
    author_email='mythmon@gmail.com',
    url='https://www.github.com/hamperbot/hamper',
    packages=find_packages(),
    install_requires=[
        "PyYAML==3.10",
        "SQLAlchemy==0.9.7",
        "Twisted==12.2.0",
        "upsidedown==0.3",
        "zope.interface==4.0.1",
        "pyOpenSSL==0.13.1",
        "requests==2.0.1",
        "flake8==2.1.0",
        "pytz==2014.3",
    ],
    extras_require={
        "postgres": ["psycopg2"],
    },
    entry_points={
        'console_scripts': [
            'hamper = hamper.commander:main',
        ],
        'hamperbot.plugins': [
            'karma = hamper.plugins.karma:Karma',
            'friendly = hamper.plugins.friendly:Friendly',
            'bitly = hamper.plugins.bitly:Bitly',
            'channel_utils = hamper.plugins.channel_utils:ChannelUtils',
            'lmgtfy = hamper.plugins.commands:LetMeGoogleThatForYou',
            'rot13 = hamper.plugins.commands:Rot13',
            'quit = hamper.plugins.commands:Quit',
            'dice = hamper.plugins.commands:Dice',
            'sed = hamper.plugins.commands:Sed',
            'lookup = hamper.plugins.dictionary:Lookup',
            'factoids = hamper.plugins.factoids:Factoids',
            'flip = hamper.plugins.flip:Flip',
            'botsnack = hamper.plugins.friendly:BotSnack',
            'ponies = hamper.plugins.friendly:OmgPonies',
            'goodbye = hamper.plugins.goodbye:GoodBye',
            'help = hamper.plugins.help:Help',
            'yesno = hamper.plugins.questions:YesNoPlugin',
            'choices = hamper.plugins.questions:ChoicesPlugin',
            'quotes = hamper.plugins.quotes:Quotes',
            'remindme = hamper.plugins.remindme:Reminder',
            'roulette = hamper.plugins.roulette:Roulette',
            'seen = hamper.plugins.seen:Seen',
            'suggest = hamper.plugins.suggest:Suggest',
            'timez = hamper.plugins.timez:Timez',
            'tinyurl = hamper.plugins.tinyurl:Tinyurl',
        ],
    },

)
