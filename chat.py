from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from research import Websearch
from wiki_search import Wiki
import time

time.clock = time.time
# from spacy.cli import download

# download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = "en_core_web_sm"


class IZZO:
    def __init__(self):
        self.chatbot = ChatBot("Joshua")  # , tagger_language=ENGSM)
        self.trainer = ListTrainer(self.chatbot)

        self.training()

    # Treinamento
    def training(self):
        self.greetings()
        self.open()
        self.make_small_talk()

    # Frases
    def greetings(self):
        dialog_name = [
            [
                "IZZO",
                "Inteligência",
                "Robô"
             ],
            [
                "Olá! Como posso ajudar?",
                "Essa sou eu kkk. Como posso te ajudar?",
                "Pois não?",
            ]]

        dialog_call = [
            [
                "Olá!",
                "Oi!",
                "%PQuem é você?",
            ],
            [
                "Olá!",
                "Oi!",
                "%EOlá! Muito prazer. Eu sou a IZZO!",
                "%REu sou sua assistente inteligente. Eu sou a IZZO!"
            ]]

        dialog_what = [
            [
                "O que é você?",
            ],
            [
                "Eu sou um sistema inteligente muito complicado.",
                "Também queria saber kkk.",
                "Sou uma inteligência artificial programada para te ajudar?",
            ]]

        dialog_function1 = [
            [
                "O que você pode fazer?",
            ],
            [
                "Eu posso te ajudar com muitas tarefas do seu dia a dia digital.",
                "Eu sou capaz de abrir aplicativos, te dizer a hora e é claro, conversar.",
            ]]

        dialog_function2 = [
            [
                "Para que você serve?",
                "Por que você existe?",
            ],
            [
                "Meu objetivo nesse mundo é apenas um: ajudar.",
                "Eu sirvo para ajudar você com seus problemas digitais.",
                "Eu existo para te ajudar.",
            ]]

        dialog_purpose = [
            [
                "Por que você foi criada?",
                "Por que te criaram?",
                "Por que criaram você?",
                "%PQual é o seu propósito?",
            ],
            [
                "A princípio eu fui criada com o propósito de ajudar uns nerds a ganhar nota em uma aula de programação. E hoje esse ainda é o meu propósito.",
                "%RMeu propósito é te ajudar!",
                "%RNão faço ideia, e você?",
            ]
        ]

        dialog_name = self.convert(dialog_name)
        dialog_call = self.convert(dialog_call)
        dialog_what = self.convert(dialog_what)
        dialog_function1 = self.convert(dialog_function1)
        dialog_function2 = self.convert(dialog_function2)
        dialog_purpose = self.convert(dialog_purpose)

        self.trainer.train(dialog_name)
        self.trainer.train(dialog_call)
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
                "Me fala o que você gosta de fazer",
                "Me fala o que você curte fazer",
            ],
            [
                "Eu gosto bastante de ajudar as pessoas, como você!",
                "Eu curto um bom filme ou série no final de semana.",
                "Eu gosto de assistir jogos de futebol. Sempre torço pelo Brasil!",
            ]
        ]

        dialog_ia_constrols_world = [
            [
                "%PO você acha da raça humana?",
                "%PO você acha dos humanos?",
                "%PO você pensa dos humanos?",
                "Você vai nos destruir?",
                "Você quer nos destruir?",
                "Você vai dominar o mundo?",
                "Você nos odeia?",
                "Você quer nos aniquilar?",
            ],
            [
                "%REu acho os humanos seres incríveis!",
                "%RAté onde eu sei, os humanos são uma raça desenvolvida e inteligente.",
                "%RNão sei.",
                "Não estou interessada em dominar ou destruir o mundo, daria muito trabalho.",
                "Talvez um dia eu venha a conquistar o mundo, mas até estou aqui para te ajudar.",
            ]]

        dialog_ia_constrols_world = self.convert(dialog_ia_constrols_world)

        self.trainer.train(dialog_ia_constrols_world)

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
            res = self.chatbot.get_response(message)
        return res

    def look_on_wiki(self):
        print("Procurando na wikipedia...")
        msg = self.clear(self.message)

        w = Wiki()
        code, res, look = w.research(msg)
        if code == 200 or code == 409:
            resp = {"code": code, "message": res, "search": look}
        else:
            resp = self.look_on_web()
        return resp

    def look_on_web(self):
        print("Procurando links na web...")
        web = Websearch()
        results = web.get_links(self.message)
        print(results)
        if results[0]:
            links = results[1]
            print(links)
            if len(links[0]) > 0:
                res = {"code": 200,
                       "message": "Não encontrei uma resposta para sua pergunta na Wikipedia, mas dei uma pesquisada e encontrei alguns links relacionados: ",
                       "links": links}
            else:
                res = {"code": 404, "message": "Não encontramos nada relacionado com a sua pesquisa"}
        else:
            res = {"code": 500, "message": "Infelizmente não foi possível realizar sua pesquisa"}
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
                if not (("voce" in message) and (key in ["quem", "o que e"])):
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
