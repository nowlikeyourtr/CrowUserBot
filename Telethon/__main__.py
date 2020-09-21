#(c)@fireganqQ - @ibrahim_cete

#code = @fireganqQ

from importlib import import_module
from Telethon.plugins import ALL_MODULES
from Telethon import LOGS, clients
import asyncio
import json
import platform
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings.json')
with open(path) as f:
    resp = json.load(f)
API_ID = resp['api_id']
API_HASH = resp['api_hash']
lang = resp['language']
loop = asyncio.get_event_loop()

async def main():
    await asyncio.gather(*[client.start() for client in clients])
    tot = 0
    enable = 0
    error = ""
    for module_name in ALL_MODULES:
        try:
            imported_module = import_module("Telethon.plugins." + module_name)
            if lang == "Turkish" or lang == "Turkce":
                LOGS.info(module_name + " Aktif.")
            elif lang == "English" or lang == "İngilizce":
                LOGS.info(module_name + " activated.")
            tot += 1
            enable += 1
        except Exception as err:
            error += module_name + " - " + str(err)
            tot += 1
    if error:
        if lang == "Turkish" or lang == "Turkce":
            LOGS.error(error + " etkinleştirilmedi.")
        elif lang == "English" or lang == "İngilizce":
            LOGS.error(error + " not activated.")
    if lang == "Turkish" or lang == "Turkce":
        LOGS.info("Etkinleştirin " + str(enable) + "/" + str(tot) + " plugins.")
    elif lang == "English" or lang == "İngilizce":
        LOGS.info("Activated " + str(enable) + "/" + str(tot) + " plugins.")

if not API_ID and not API_HASH:
    if lang == "Turkish" or lang == "Turkce":
        print("Settings.json üzerinde veya CrowUserBot u başlatarak API Kimliği ve HASH API yi yapılandırın!")
    elif lang == "English" or lang == "İngilizce":
        print("Configure the API ID and API HASH on settings.json or by starting EasyUserBot")
    exit()
else:
    loop.run_until_complete(main())
    if lang == "Turkish" or lang == "Turkce":
        LOGS.info("Tüm kullanıcı botları başarıyla başladı.")
    elif lang == "English" or lang == "İngilizce":
        LOGS.info("All userbots have started successfully.")
    loop.run_forever()
