#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("an online StringSession generator")


print("t ==> Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://github.com/JAVES-5/JAVES-5")


def Javes2():
    print("you selected Telethon")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        session_str = client.session.save()
        s_m = client.send_message("me", session_str)
        s_m.reply(
            "⬆️ This StringSession is generated using https://repl.it/@Javes786/Javes-20-String-session#main.py \nPlease subscribe https://t.me/javes_support "
        )
        print("please check your Telegram Saved Messages for the StringSession ")


Javes2()
