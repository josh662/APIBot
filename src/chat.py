from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from src.research import Websearch
from src.wiki_search import Wiki
from spacy.cli import download
import time

time.clock = time.time

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = "en_core_web_sm"

class IZZO:
    def __init__(self):
        self.chatbot = ChatBot("Izzo", tagger_language=ENGSM)
        self.trainer = ListTrainer(self.chatbot)

        self.training()

    # Treinamento
    def training(self):
        self.greetings()
        self.open()
        self.make_small_talk()
        self.addons()

    # Frases
    def greetings(self):
        dialog_name = [
            [
                "IZZO",
                "ISO", #Como o sistema entende quando o nome é falado
                "Inteligência",
                "Robô"
             ],
            [
                "Olá! Como posso ajudar?#TALKING",
                "Essa sou eu kkk. Como posso te ajudar?#TONGUE",
                "Pois não?#HAPPY",
            ]]

        dialog_call1 = [
            [
                "Olá!",
                "Oi!",
                "%PQuem é você?",
            ],
            [
                "Olá!#TALKING",
                "Oi!#TALKING",
                "Olá! Muito prazer. Eu sou a IZZO!#TALKING",
                "%REu sou sua assistente inteligente. Eu sou a IZZO!#TALKING",
                "%REu sou a IZZO!#TALKING"
            ]]

        dialog_call2 = [
            [
                "Olá tudo bem?",
                "Oi tudo bem?",
                "%POi como você está?",
            ],
            [
                "Olá, tudo sim! Obrigada por perguntar!#TALKING",
                "Olá, estou bem sim. O que posso fazer por você?#TALKING",
                "%ROlá! Estou bem. Como posso te ajudar?#HAPPY"
            ]]

        dialog_what = [
            [
                "O que é você?",
            ],
            [
                "Eu sou um sistema inteligente muito complicado.#TONGUE",
                "Também queria saber kkk.#TONGUE",
                "Sou uma inteligência artificial programada para te ajudar.#TALKING",
            ]]

        dialog_function1 = [
            [
                "O que você pode fazer?",
            ],
            [
                "Eu posso te ajudar com muitas tarefas do seu dia a dia digital. Posso te falar as horas, conversar, e abrir sites e aplicativos.#TALKING",
                "Eu sou capaz de abrir aplicativos, te dizer a hora e é claro, conversar.#TALKING",
            ]]

        dialog_function2 = [
            [
                "Para que você serve?",
                "Por que você existe?",
                "%PQuem criou você?",
                "%PQuem te criou?",
            ],
            [
                "Meu objetivo nesse mundo é apenas um: ajudar.#HAPPY",
                "Eu sirvo para ajudar você com seus problemas digitais.#HAPPY",
                "Eu existo para te ajudar.#HAPPY",
                "%REu fui criada pelos garotos de programa.#TONGUE"
            ]]

        dialog_purpose = [
            [
                "Por que você foi criada?",
                "Por que te criaram?",
                "Por que criaram você?",
                "%PQual é o seu propósito?",
            ],
            [
                "A princípio eu fui criada com o propósito de ajudar uns nerds a ganhar nota em uma aula de programação. E hoje esse ainda é o meu propósito.#TONGUE",
                "%RMeu propósito é te ajudar!#TALKING",
                "%RNão faço ideia.#TALKING",
            ]]

        dialog_name = self.convert(dialog_name)
        dialog_call1 = self.convert(dialog_call1)
        dialog_call2 = self.convert(dialog_call2)
        dialog_what = self.convert(dialog_what)
        dialog_function1 = self.convert(dialog_function1)
        dialog_function2 = self.convert(dialog_function2)
        dialog_purpose = self.convert(dialog_purpose)

        self.trainer.train(dialog_name)
        self.trainer.train(dialog_call1)
        self.trainer.train(dialog_call2)
        self.trainer.train(dialog_what)
        self.trainer.train(dialog_purpose)
        self.trainer.train(dialog_function1)
        self.trainer.train(dialog_function2)

        # print(dialog_name)

    def open(self):
        websites = {
            # Google
            "YouTube": "https://www.youtube.com/",
            "Google":"https://www.google.com/",

            # Redes Sociais
            "Facebook": "https://www.facebook.com/",
            "WhatsApp": "https://web.whatsapp.com/",
            "Instagram": "https://www.instagram.com/",
            "Twitter": "https://twitter.com/",
            "Tik Tok": "https://www.tiktok.com/",
            "TikTok": "https://www.tiktok.com/",

            # Sites de compras online
            "Amazon": "https://www.amazon.com.br/",
            "Mercado Livre": "https://www.mercadolivre.com.br/",
            "OLX": "https://www.olx.com.br/",
            "Shopee": "https://shopee.com.br/",
            "Casas Bahia": "https://www.casasbahia.com.br/",
            "Magazine Luiza": "https://www.magazineluiza.com.br/",
            "Magalu": "https://www.magazineluiza.com.br/",
            "Correios": "https://www.correios.com.br/",

            # Sites de trabalho
            "Linkedin": "https://www.linkedin.com/",

            # Sites do governo
            "site do governo": "https://www.gov.br/",
            
            # Sites de Streaming
            "Netflix": "https://www.netflix.com/",
            "Paramount": "https://www.paramountplus.com/",
            "Amazon Prime Video": "https://www.primevideo.com",
            "Disney": "https://www.disneyplus.com/",
            "Disney plus": "https://www.disneyplus.com/",
            "Disney +": "https://www.disneyplus.com/",
            "HBO Max": "https://www.hbomax.com",
        }

        dialog_website = []

        for site in websites.keys():
            phrases = []
            website = []
            phrases.append(f"Abrir o {site}")
            phrases.append(f"Abrir a {site}")
            phrases.append(f"Abrir o site {site}")
            phrases.append(f"Iniciar o {site}")
            phrases.append(f"Iniciar {site}")
            phrases.append(f"Abra o {site}")
            phrases.append(f"Abra a {site}")
            phrases.append(f"Abra o site {site}")
            phrases.append(f"Me mande para o {site}")
            phrases.append(f"Me mande para a {site}")
            website.append(f"%OPEN:{websites[site]}")

            for phrase in phrases:
                for link in website:
                    dialog_website.append(phrase)
                    dialog_website.append(link)

        self.trainer.train(dialog_website)
        # print(dialog_website)

    def make_small_talk(self):  # Jogar conversa fora
        dialog_hobby = [
            [
                "O que você gosta de fazer?",
                "O que você curte?",
                "Do que você gosta?",
                "O que você faz no seu tempo livre?"
                "Me fala o que você gosta de fazer",
                "Me fala o que você curte fazer",
            ],
            [
                "Eu gosto bastante de ajudar as pessoas, como você!#HAPPY",
                "Eu curto um bom filme ou série no final de semana.#HAPPY",
                "Eu gosto de assistir jogos de futebol. Sempre torço pelo Brasil!#TONGUE",
            ]
        ]

        dialog_food = [
            [
                "O que você gosta de comer?",
                "Qual é a sua comida favorita?",
                "De que comida você gosta?",
                "Qual comida você mais gosta?",
            ],
            [
                "Sou uma inteligência artificial, então nunca comi nada, mas se pudesse, ouvi dizer que sorvete é muito bom!#HAPPY",
                "Eu infelizmente não sou humana como você para experimentar comidas deliciosas.#ANGRY"
                "Eu nunca comi nada de verdade, mas já experimentei um emoji de brigadeiro.#TALKING"
            ]
        ]

        dialog_ia_constrols_world = [
            [
                "%PO você acha da raça humana?",
                "%PO você acha dos humanos?",
                "%PO você pensa dos humanos?",
                "%PO que acha da raça humana?",
                "Você vai nos destruir?",
                "Você quer nos destruir?",
                "Você vai dominar o mundo?",
                "Você nos odeia?",
                "Você quer nos aniquilar?",
            ],
            [
                "%REu acho os humanos seres incríveis!#TALKING",
                "%RAté onde eu sei, os humanos são uma raça desenvolvida e inteligente.#THINKING",
                "%RNão sei.#THINKING",
                "Não estou interessada em dominar ou destruir o mundo, daria muito trabalho.#TONGUE",
                "Talvez um dia eu venha a conquistar o mundo, mas até lá estou aqui para te ajudar.#TALKING",
            ]]

        dialog_user = [
            [
                "Você gosta de mim?",
                "%PVocê namora?",
                "%PVocê tem namorado?",
                "O que você acha de mim?",
                "O que você acha sobre mim?"
            ],
            [
                "%REu não tenho namorado. Sou livre, leve e solta.#TONGUE",
                "Eu gosto muito de você!#TALKING",
                "Eu acho você uma pessoa incrível!#HAPPY"
            ]
        ]

        dialog_age = [
            [
                "Quantos anos você tem?",
                "Qual é a sua idade?",
                "%PEm que ano você nasceu?"
            ],
            [
                "Minha idade é um segredo bem guardado!#TONGUE",
                "Sou mais nova que você.#TONGUE",
                "%REu nasci em 2022.#HAPPY"
            ]
        ]

        dialog_location = [
            [
                "%PDe onde você é?",
                "%PDe onde é você?",
                "%PDe onde você vêm?",
                "%PAonde você mora?",
                "Você é brasileira?"
            ],
            [
                "Eu sou uma brasileira nata!#HAPPY",
                "%REu fui pensada e criada no Brasil, mais especificamente na cidade de Ribeirão Preto!#TALKING",
                "%REu sou de Ribeirão Preto, interior de São Paulo e moro com os meus criadores: Os garotos de programa.#TONGUE",
            ]
        ]

        dialog_hobby = self.convert(dialog_hobby)
        dialog_food = self.convert(dialog_food)
        dialog_ia_constrols_world = self.convert(dialog_ia_constrols_world)
        dialog_user = self.convert(dialog_user)
        dialog_age = self.convert(dialog_age)
        dialog_location = self.convert(dialog_location)

        self.trainer.train(dialog_hobby)
        self.trainer.train(dialog_food)
        self.trainer.train(dialog_ia_constrols_world)
        self.trainer.train(dialog_user)
        self.trainer.train(dialog_age)
        self.trainer.train(dialog_location)

    def addons(self):
        dialog_thanks = [
            [
                "Muito obrigado!",
                "Obrigado!",
                "Agradeço!"
            ],
            [
                "Não tem de quer!#HAPPY",
                "Magina.#HAPPY",
                "Magina. Precisando é só chamar!#HAPPY",
                "O prazer foi meu!#HAPPY"
            ]
        ]

        dialog_laud = [
            [
                "Você é muito esperta!",
                "Você é muito inteligente!",
                "Você é legal!"
            ],
            [
                "Obrigada!#TALKING"
            ]
        ]

        dialogs_ignore = [
            [
                "%PEntendi",
                "Certo",
                "Legal",
                "Interessante",
                "Não sei"
            ],
            [
                "%RQue bom.#HAPPY",
                "Okay.#HAPPY"
            ]
        ]

        dialog_tired = [
            [
                "Eu estou cansado.",
                "Estou cansado.",
                "Quero dormir.",
                "Estou com sono"
            ],
            [
                "Que tal ir tirar um cochilo? Eu tomo conta de tudo!#TALKING",
                "Que tal ir tirar um cochilo?#TALKING",
                "Que tal um cochilo?#TALKING",
                "Ora, então vá descansar!#HAPPY"
            ]
        ]

        dialog_thanks = self.convert(dialog_thanks)
        dialog_laud = self.convert(dialog_laud)
        dialogs_ignore = self.convert(dialogs_ignore)
        dialog_tired = self.convert(dialog_tired)

        self.trainer.train(dialog_thanks)
        self.trainer.train(dialog_laud)
        self.trainer.train(dialogs_ignore)
        self.trainer.train(dialog_tired)

    # Sistema de chat e pesquisa
    def chat(self, message):
        self.message = message
        is_search = self.is_search(self.message)
        if is_search[0]:
            if is_search[1]:
                res = self.look_on_web()
            else:
                res = self.look_on_wiki()
        else:
            if "que horas são" in message.lower():
                horas = time.strftime("Agora são %H horas e %M minutos, no horário de Brasília.")
                res = {"code": 200, "message": horas, "talk": horas, "feeling": "THINKING", "command": False}
            else:
                code = 200
                msg = str(self.chatbot.get_response(message))
                if "#" in msg:
                    feeling = msg.split("#")[1]
                    msg = msg.split("#")[0]
                else:
                    feeling = "TALKING"
                talk = msg
                command = False
                if "%OPEN" in msg:
                    command = True
                    talk = "Abrindo o site!"
                res = {"code": code, "message": msg, "talk": talk, "feeling": feeling, "command": command}
        return res

    def look_on_wiki(self):
        print("Procurando na wikipedia...")
        msg = self.clear(self.message)

        w = Wiki()
        code, res, look, link = w.research(msg)
        if code == 200 or code == 409:
            resp = {"code": code, "talk": fr"Segundo a Wikipedia {res}. Para saber mais procure por {look}", "feeling": "TALKING", "command": False,
                    "message": fr"Segundo a Wikipedia, '{res}'. Para saber mais procure por '{look}' na internet ou acesse esse link: {link}."}
        else:
            resp = self.look_on_web()
        return resp

    def look_on_web(self):
        print("Procurando links na web...")
        web = Websearch()
        results = web.get_links(self.message)
        # print(results)
        if results[0]:
            links = results[1]
            # print(links)
            if len(links[0]) > 0:
                websites = links[0]
                webvideos = links[1]
                print(websites)
                print(webvideos)

                if len(websites) >= 3:
                    sites = ""
                    cont = 0
                    for site in websites:
                        sites += f"'{site}'\n"
                        cont += 1
                        if cont >= 3:
                            break
                else:
                    sites = websites[0]

                if len(webvideos) >= 3:
                    videos = ""
                    cont = 0
                    for video in webvideos:
                        videos += f"'{video}'\n"
                        cont += 1
                        if cont >= 2:
                            break
                else:
                    videos = webvideos[0]
                res = {"code": 200,
                       "talk": "Não encontrei uma resposta para sua pergunta, mas pesquisei na internet e espero que esses sites ou videos possam te ajudar", "command": False,
                       "message": f"Não encontrei uma resposta válida.\n\nSites relacionados:\n\n{sites}\n\nVideos do YouTube:\n\n{videos}", "feeling": "THINKING"}
            else:
                res = {"code": 404, "talk": "Não encontramos nada relacionado com a sua pesquisa", "command": False,
                       "message": "Não encontramos nada relacionado com a sua pesquisa", "feeling": "THINKING"}
        else:
            res = {"code": 500, "talk": "Infelizmente não foi possível realizar sua pesquisa", "command": False,
                   "message": "Infelizmente não foi possível realizar sua pesquisa", "feeling": "ANGRY"}
        return res

    # Outras funções
    def convert(self, array):
        big_array = []
        for key in array[0]:
            for value in array[1]:
                add = True

                if key == value:
                    add = False

                if ("%P" in key) and (("%R" not in value) and ("%E" not in value)):
                    add = False

                if ("%P" not in key) and ("%R" in value):
                    add = False

                if add:
                    key = self.tag_remover(key)
                    value = self.tag_remover(value)

                    big_array.append(key)
                    big_array.append(value)
        return big_array

    def tag_remover(self, text):
        tags = ["P", "R", "E"]

        for tag in tags:
            text = text.replace(f"%{tag}", "")
        return text

    def is_search(self, message):
        message = message.lower()
        message = message.replace("ê", "e")
        message = message.replace("é", "e")

        search_keys = ["quem", "quando", "onde", "como", "porque", "o que e"]

        ask_how_where = False

        for key in search_keys:
            if message.find(key) == 0:
                if not (("voce" in message or "criou" in message) and (key in ["quem", "o que e"])):
                    if key in ["onde", "como"]:
                        ask_how_where = True
                    return True, ask_how_where
        return False, ask_how_where

    def clear(self, message):
        search_keys = ["quem foi", "quem é", "quando foi",
                       "onde fica", "onde", "como", "porque", "o que e", "é", "foi", "está",
                       "esta", "?", "!", ".", " a "]

        message = message.lower()
        for key in search_keys:
            message = message.replace(key, " ")
            message = message.replace("  ", " ")

        message = message.strip().capitalize()

        return message

if __name__ == "__main__":
    bot = IZZO()
    print("Eaiii!")
    while True:
        txt = input(">| ")
        if txt != "":
            res = bot.chat(txt)
            print(f"# {res}")
