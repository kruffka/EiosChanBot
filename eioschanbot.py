# -*- coding: utf-8 -*-
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time
import urllib.request
from vk_api.utils import get_random_id
import os
from datetime import datetime
import re
import imgur_url
import json

url = imgur_url.ImgurURL()
#
# anime_list = {
#     "artwork4k": [
#         "nAud4OF"
#     ],
#     "5sm": [
#         "KFTuR"
#     ],
#     "akame": [
#         "q5d9q"
#     ],
#     "akira": [
#         "EaJVW"
#     ],
#     "aldnoah": [
#         "doW0O"
#     ],
#     "amagi": [
#         "EECoy"
#     ],
#     "angelbeats": [
#         "D6RtK"
#     ],
#     "another": [
#         "cl39U"
#     ],
#     "aot": [
#         "70qzC"
#     ],
#     "baccano": [
#         "P1fXp"
#     ],
#     "blackbullet": [
#         "JIvlI"
#     ],
#     "bleach": [
#         "ilPO0"
#     ],
#     "chuunibyou": [
#         "DsCmU"
#     ],
#     "codegeass": [
#         "f7Wgy"
#     ],
#     "bebop": [
#         "r4Brd"
#     ],
#     "danmachi": [
#         "Fv1A1"
#     ],
#     "deadman": [
#         "Bj4AU"
#     ],
#     "deathnote": [
#         "iiYMv"
#     ],
#     "durarara": [
#         "8vcsN"
#     ],
#     "elfen": [
#         "VBEbf"
#     ],
#     "expelled": [
#         "zcaOM"
#     ],
#     "flcl": [
#         "Vt7p7"
#     ],
#     "fma": [
#         "DwHHd"
#     ],
#     "fate": [
#         "O0zZx"
#     ],
#     "girlspanzer": [
#         "jghyU"
#     ],
#     "goldentime": [
#         "7R8e4"
#     ],
#     "guiltycrown": [
#         "1nPyW", "2WhnW"
#     ],
#     "ghostshell": [
#         "3GRg1"
#     ],
#     "gurren": [
#         "sTtPF", "lTOjG"
#     ],
#     "haganai": [
#         "rXs1K"
#     ],
#     "hellsing": [
#         "rH702"
#     ],
#     "haruhi": [
#         "YulaA"
#     ],
#     "dxd": [
#         "wvwQY", "RaY9Z"
#     ],
#     "higurashi": [
#         "2FxgQ"
#     ],
#     "hitsugi": [
#         "6xe5f"
#     ],
#     "hxh": [
#         "ObHQG", "Ty3VX", "IKi27"
#     ],
#     "jojo": [
#         "7ZvXt"
#     ],
#     "joshiraku": [
#         "rr95o"
#     ],
#     "hetai": [
#         "V8ey3", "lxSc3", "D0rV4", "drBFx", "WbogB"
#     ],
#     "katanagatari": [
#         "T9fou"
#     ],
#     "killlakill": [
#         "6Swch", "iaIpI", "iVGg0"
#     ],
#     "k-on": [
#         "Y8Ket", "qpAIo", "klNv5"
#     ],
#     "koufuku": [
#         "p50O0"
#     ],
#     "kyoukai": [
#         "kAJJB"
#     ],
#     "littlewitch": [
#         "ZqCIG"
#     ],
#     "loghorizon": [
#         "9bJVI"
#     ],
#     "lovelive": [
#         "PS49L", "6h7Te"
#     ],
#     "mekaku": [
#         "Ji2mK"
#     ],
#     "mikankunin": [
#         "qJqdr"
#     ],
#     "mirai": [
#         "tQVoG", "gph54"
#     ],
#     "musume": [
#         "B40YU"
#     ],
#     "eva": [
#         "xjZa1", "bYFOf"
#     ],
#     "nichijou": [
#         "SZbKu"
#     ],
#     "nisekoi": [
#         "bfm9x"
#     ],
#     "ngnl": [
#         "wsui9"
#     ],
#     "onepunch": [
#         "TgOGs", "2k6yr"
#     ],
#     "panty": [
#         "X62dw"
#     ],
#     "prisonschool": [
#         "NQF2q"
#     ],
#     "psychopass": [
#         "p18tX"
#     ],
#     "madoka": [
#         "INvy3", "RP80K", "pHBa9"
#     ],
#     "railwars": [
#         "YexS2"
#     ],
#
#     "rezero": [
#         "L8laF"
#     ],
#
#     "rezerobest": [
#         "KU8QA"
#     ],
#
#     "rollinggirls": [
#         "hSrk8"
#     ],
#     "rbwy": [
#         "hUwbn", "gNIdX"
#     ],
#
#     "saekano": [
#         "F0zky"
#     ],
#     "sakamichi": [
#         "NVM6T"
#     ],
#     "sakura": [
#         "iEAMV"
#     ],
#     "champloo": [
#         "ndwlS"
#     ],
#     "serialexperiments": [
#         "oeA76"
#     ],
#     "steinsgate": [
#         "ptgIk", "LkfQa", "dARAq", "QyWlE"
#     ],
#     "shingeki": [
#         "jOF4X"
#     ],
#     "sonico": [
#         "MeEDh", "YLT3Q"
#     ],
#     "sao": [
#         "bWpV1", "PzE2o"
#     ],
#     "shokugeki": [
#         "tbzH3"
#     ],
#     "souleater": [
#         "byRKr"
#     ],
#     "spacedandy": [
#         "h8yVX"
#     ],
#     "spicewolf": [
#         "aBxIf"
#     ],
#     "strikewitches": [
#         "byciO"
#     ],
#     "thedevilparttime": [
#         "61hhE"
#     ],
#     "toradora": [
#         "Cakrp"
#     ],
#     "ghoul": [
#         "SiD5T", "fSMGy"
#     ],
#     "trigun": [
#         "SfKuO"
#     ],
#
#     "tengentoppa": [
#         "F1x52"
#     ],
#
#     "vocaloid": [
#         "htn7y"
#     ],
#
#     "upotte": [
#         "3xU9E"
#     ],
#
#     "watamote": [
#         "eRh92"
#     ],
#
#     "welcometonhk": [
#         "YFlL0"
#     ],
#
#     "yuruyuri": [
#         "PcXM2"
#     ],
#     "yourlieinapril": [
#         "Nbo0l"
#     ],
#     "zankyou": [
#         "dNL0J"
#     ],
#     "mechawallpapers": [
#         "xRJc3"
#     ],
#     "gundam": [
#         "7lZ0s"
#     ],
#     "bakemonogatari": [
#         "SyXf1"
#     ],
#     "monogatari": [
#         "0pGnO"
#     ],
#     "discrete": [
#         "wBNb8", "vP62K", "jZgsR", "BEOrj", "1StJV", "NMUvE", "PFBbI", "opmvJ"
#     ],
#     "discretebg": [
#         "8QKvH", "IHyPl", "XRAfu", "veQcQ", "nxY0Q"
#     ],
#     "minimalism": [
#         "sygy2"
#     ],
#     "shinobu4k": [
#         "Zygsg"
#     ],
#     "ganbatte": [
#         "QHtcw"
#     ],
#     "mobilewallpaper": [
#         "l2Wpf"
#     ],
#     "christmas": [
#         "Yuj1Jbl"
#     ]
# }
#
# with open('anime_albums.json', 'w') as outfile:
#     json.dump(anime_list, outfile)

with open('anime_albums.json', 'r') as openfile:
    anime_list = json.load(openfile)

# hash = anime_list["5sm"]
# print(anime_list)
# # print(url.get_imgur_urls('imgur.com/a/' + hash)[0])
# anime_name = "5sm"


# with open("/home/eios/crashs/time.txt", "w") as file:
#     file.write(datetime.now().strftime("%d-%m-%Y\n%X"));


eios_msg = ["eios", "eioschan", "eios chan", "ёся", "ёсятян", "ёся тян", "ёсячан", "ёся чан", "еся", "еся тян", "есятян", "есячан", "еся чан", "эиос", "еиос", "imouto", "имото", "сестричка"]
sbs_msg = ["братик", "брат", "сибгути", "sibsutis", "сибгучи", "sibguti", "сибсутис", "анисан", "ани сан", "они сан", "онисан"]
bad_word = ["иблан", "иблан.", "бака", "бака.", "дурак", "дурак.", "дура", "дура.", "ибалайка", "ибалайка.", "гейка", "гейка."]
roll = ["roll", "ролл", "hjkk", "кщдд"]

sbs_sleep = [
    "https://www.youtube.com/watch?v=YpCqxf9p02o"
]
sbs_not_sleep = [
    "Братик не спит!~"
]

eios_sleep = [
    "Я в своем сне так преисполнилась, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля, мне этот мир абсолютно понятен, и я здесь ищу только одного - покоя, умиротворения и вот этой гармонии, от слияния с бесконечно вечным, от созерцания великого фрактального подобия и от вот этого замечательного всеединства существа, бесконечно вечного, куда ни посмотри, хоть вглубь - бесконечно малое, хоть ввысь - бесконечно большое, понимаешь?",
    "Жизнь и сновидения — страницы одной и той же книги.",
    "Сны — грандиозный сериал подсознания.", "Спящему не достанется ничего, кроме снов.", "Сон - самый лучший вид релакса.",
    "Чем лучше сон, тем больше хочется в нём проснуться.", "Жизнь тем и интересна, что в ней сны могут стать явью. - Пауло Коэльо",
    "Сон — как раз единственный отрезок времени, когда мы свободны. Во сне мы позволяем нашим мыслям делать, что им хочется. - Бернар Вербер",
    "Чем более странным нам кажется сон, тем более глубокий смысл он несет. - Зигмунд Фрейд",
    "Когда нечего есть, лучше лечь спать. Когда плохое настроение, лучше лечь спать. Проснёшься — уже в порядке. А если не выходит, лучше опять лечь спать. - Земфира Рамазанова",
    "Я вижу сны. Иногда мне кажется, что это единственное правильное занятие на свете. - Харуки Мураками",
    "Мы сотканы из ткани наших снов. - Уильям Шекспир",
    "Три вещи дарованы нам, чтобы смягчить горечь жизни: смех, сон и надежда. - Мария Домбровская",
    "Сон, прекраснейшее из наслаждений жизни, в отличие от других, не утомляет и не приедается. - Роджер Желязны",
    "Единственная вещь в этой жизни, которая меня действительно занимает – это сон. Я люблю спать так долго, как только могу. - Кристиан Бейл",
    "В любом сне, детка, главное — вовремя проснуться. - Мариам Петросян",
    "Если хочешь крепко спать, возьми с собой в постель чистую совесть. - Бенджамин Франклин",
    "Пару раз в жизни я действительно испытывал настоящее счастье. И оба раза просыпался. - Майкл Питт",
    "Не хочу видеть сны. Я хочу просто спать. - Пол Тот",
    "На мой взгляд, спать надо долго и со вкусом, а просыпаться как можно позже. - Макс Фрай",
    "Крепче всего спят не те, у кого чистая совесть, а те, у кого её отродясь не бывало. - Борис Акунин",
    "Задремала на минутку (x.x)~~zzZ",
    "F"

]

eios_not_sleep = [
    "За одну бессонную ночь узнаешь больше, чем за год сна.",
    "Бессонница — это насилие ночи над человеком.",
    "Кто не страдал бессонницей, тот не знает своей биографии.",
    "Я не сплю!~",
    "Го встр)"
]

russia = [
    "россия.", "россия", "russia.", "russia", "раша", "раша.", "рашка", "рашка.",
    "российская федерация", "российская федерация.", "рф", "рф.", "rf", "rf.",
    "russian federation.", "russian federation",
    "рассия", "расея", "рассия.", "расея.", "рассея.", "рассея.",
    "россия?", "раша?", "рашка?", "россия!"
    ]

response = 0

token = "token_here"

vk = vk_api.VkApi(token=token)

vk._auth_token()

api = vk.get_api()

longpoll = VkBotLongPoll(vk, 'id_here')

def anime(user_id, folder):
            try:
                hash = anime_list[folder][random.randint(0, len(anime_list[folder]) - 1)]

                link_arr = url.get_imgur_urls('imgur.com/a/' + hash)
                link = link_arr[random.randint(0, len(link_arr) - 1)]

                # download image to host
                dl = requests.get(link)
                out = open("anime\img.jpg", "wb")
                out.write(dl.content)
                out.close()

                # load to vk

                a = vk.method("photos.getMessagesUploadServer")
                path = "anime\img.jpg"
                b = requests.post(a['upload_url'], files={'photo': open(path, 'rb')}).json()
                c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                vk.method("messages.send", {"peer_id": user_id, "message": "", "attachment": f'photo{c["owner_id"]}_{c["id"]}', "random_id":get_random_id()})

                # delete from host
                os.remove("anime\img.jpg")

            except Exception as e:
                pass


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj['message']

        peer_id = message['peer_id']
        text = message['text']

        for eios in eios_msg:
            if text.lower() == eios:
                # try:
                #     response = urllib.request.urlopen("https://eios.sibsutis.ru/").getcode()
                # except Exception as E:
                #     time.sleep(0)
                #     #response = 0

                #if (response == 200):

               # else:
                msg = random.randint(0, len(eios_sleep) - 1)
                api.messages.send(peer_id=peer_id, message=eios_sleep[msg], random_id=get_random_id())

        if text.lower() == "еся не спит" or text.lower() == "no sleep" or text.lower() == "не спит":
            msg = random.randint(0, len(eios_not_sleep) - 1)
            api.messages.send(peer_id=peer_id, message=eios_not_sleep[msg], random_id=get_random_id())

        for sbs in sbs_msg:
            if text.lower() == sbs:
                try:
                    response = urllib.request.urlopen("https://sibsutis.ru").getcode()
                except Exception as E:
                    time.sleep(0)
                    #response = 0

                if (response == 200):
                    msg = random.randint(0, len(sbs_not_sleep) - 1)
                    api.messages.send(peer_id=peer_id, message=sbs_not_sleep[msg], random_id=get_random_id())
                else:
                    msg = random.randint(0, len(sbs_sleep) - 1)
                    api.messages.send(peer_id=peer_id, message=sbs_sleep[msg], random_id=get_random_id())

        for bad in bad_word:
            if text.lower() == bad:
                api.messages.send(peer_id=peer_id, message="Baka!~", random_id=get_random_id())


        for rl in roll:
            if text.lower()[:4] == rl:
                roll_resp = random.randint(1, 100)

                if len(text.lower()) > 4:
                    nums = re.findall(r'\d+', text.lower()[5:])
                    if(len(nums) == 1):
                        try:
                            roll_resp = random.randint(1, int(nums[0]))
                        except Exception as E:
                            time.sleep(0)
                            roll_resp = "0 не натуральное число!~ Бака!~"
                    elif(len(nums) == 2):
                        try:
                            roll_resp = random.randint(int(nums[0]), int(nums[1]))
                        except Exception as E:
                            time.sleep(0)
                            roll_reps = "Два натур. числа в возрастающем порядке!~ Бака?~"
                nums = 0
                api.messages.send(peer_id=peer_id, message=roll_resp, random_id=get_random_id())


        if text.lower() == "ссср" or text.lower() == "союз" or text.lower() == "loli" or text.lower() == "лоли":
            api.messages.send(peer_id=peer_id, message="https://www.youtube.com/watch?v=VWaQcKiAj_Q", random_id=get_random_id())

        for ruske in russia:
            if text.lower() == ruske:
                api.messages.send(peer_id=peer_id, message="https://www.youtube.com/watch?v=HwrsdoepIjc", random_id=get_random_id())

        if text.lower() == "ded" or text.lower() == "дед" or text.lower() == "rip" or text.lower() == "рип":
            api.messages.send(peer_id=peer_id, message="https://www.youtube.com/watch?v=YpCqxf9p02o", random_id=get_random_id())

        if text.lower() == "я устал" or text.lower() == "я устала" or text.lower() == "устал" or text.lower() == "устала":
            api.messages.send(peer_id=peer_id, message="Поспи!~", random_id=get_random_id())


        if text.lower()[:4] == "http":
            try:
                response = urllib.request.urlopen("https://{}".format(text.lower()[5:])).getcode()
            except Exception as E:
                time.sleep(0)
                response = "rip"

            api.messages.send(peer_id=peer_id, message="Http:{}".format(response), random_id=get_random_id())
            response = "Го встр)"
        #
        if text.lower() == "anime" or text.lower() == "аниме":
            api.messages.send(peer_id=peer_id, message="Список моих альбомов: {} ( ◞･౪･)\n Источник: https://www.reddit.com/r/anime/comments/6kfngy/anime_wallpapers_40000_images_100_anime_5000_nsfw/".format(str(anime_list.keys())[9:]),
                              random_id=get_random_id())

        if text.lower()[:6] == "anime " or text.lower()[:6] == "аниме ":
            check = 0
            for list in anime_list:
                if (list == text.lower()[6:]):
                    anime(peer_id, text.lower()[6:])
                    check = 1
            if(check == 0):
                api.messages.send(peer_id=peer_id, message="У меня такого, наверное, нету~ (⌣_⌣”) Напиши 'аниме', чтобы увидеть список!~", random_id=get_random_id())

        if text.lower() == "tcz":
            api.messages.send(peer_id=peer_id, message="Cfv nfrjq", random_id=get_random_id())

        if text.lower() == "k-on" or text.lower() == "keion" or text.lower() == "кейон" or text.lower() == "к-он":
            anime(peer_id, "k-on")

        if text.lower() == "с днем овощного рагу" or text.lower() == "с днем овощного рагу!":
            a = vk.method("photos.getMessagesUploadServer")
            b = requests.post(a['upload_url'], files={'photo': open("aarUXeal2Sg.jpg", 'rb')}).json()
            c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
            vk.method("messages.send",
                      {"peer_id": peer_id, "message": "С днем овощного рагу!", "attachment": f'photo{c["owner_id"]}_{c["id"]}',
                       "random_id": get_random_id()})






