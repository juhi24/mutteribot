mutteribot
==========

A `Telegram bot <https://telegram.org/blog/bot-revolution>`_ that uses `Ruuvi weather station <https://ruu.vi/setup/#weather-station>`_ data generated with `ilmaruuvi <https://github.com/juhi24/ilmaruuvi>`_


Installation
------------

Make sure you have setuptools installed and run (as root)::

    python setup.py install


Getting started
---------------

1. Get your Telegram API key by talking to `@BotFather <https://telegram.me/botfather>`_

2. Configure at ``/etc/mutteribot.conf``

3. Start the bot::

    systemctl start mutteribot