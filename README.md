#### PingEcho server info
Returns datetime from a server with the `info` command


#### Requeriments
- Python 3.7.x
- Create a [Telegram Account](https://web.telegram.org/)
- Create a bot with [BotFather](https://core.telegram.org/bots#6-botfather)
- Install: `pip3 install python-telegram-bot --upgrade`

#### Setting
Modify `app.py` to set the bot's token

```
updater = Updater(token='BotToken', use_context=True)
```

#### Commands
```
/start
I'm a bot, please talk to me!
```

```
/info
Server time: 2020-12-11 10:07:39.621375
```

#### Docs
- [python-telegram-bot/wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)