# -*- coding: utf-8 -*-
import telegram
import config

def main():
    conf = config.initialize_config()
    token = conf['general']['token']
    if len(token)<1:
        raise Exception('Token not set.')
    bot = telegram.Bot(token=token)
    print(bot.getMe())
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()