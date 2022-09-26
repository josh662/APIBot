import wikipedia
import wikipediaapi

class Wiki:
    def __init__(self):
        pass

    def research(self, search):
        res = ""
        self.search = search
        wikipedia.set_lang("pt")
        self.articles = wikipedia.search(query=self.search, results=10)
        self.look = ""
        self.look = self.compare(self.search, self.articles)
        code = 200
        link = "NOT FOUND"

        if self.look != "":
            try:
                wiki = wikipediaapi.Wikipedia('pt')
                page = wiki.page(self.look)
                link = page.fullurl
                print(f"URL: {page.fullurl}")
            except Exception as err:
                print(err)

            try:
                res = wikipedia.summary(self.look, sentences=10)

            except wikipedia.exceptions.DisambiguationError:
                res = "Foram encontrados múltiplos resultados para a sua pesquisa! Poderia ser mais específico?"
                code = 409

            except Exception as err:
                print(f"Erro inesperado na busca na wikipedia!\nERRO: {err}")
                res = "Puxa, parece que tivemos um problema interno, por favor tente novamente mais tarde!"
                code = 500
        else:
            res = "Não encontramos nada relacionado com a sua pesquisa"
            code = 404

        if code == 200:
            res = res.replace(" .", ".")
            res = res.replace(". ", ".")
            res = res.replace(".", ". ")
            res = res.replace("\n", "")

            length = 400

            if len(res) > length:
                res = res[:length].strip() + "..."

        return code, res, self.look, link

    def compare(self, text, texts):
        sum_txt = 0
        min_difference = 100000000
        index = -1
        try:
            for letter in text:
                num = int(ord(letter))
                sum_txt += num

            sums_texts = []

            for txt in texts:
                sum = 0
                for letter in txt:
                    num = int(ord(letter))
                    sum += num
                sums_texts.append(sum)

            proximity = []

            for number in sums_texts:
                prox = abs(number - sum_txt)
                proximity.append(prox)

            min_difference = min(proximity)
            index = proximity.index(min_difference)

            # print(text)
            # print(sum_txt)
            # print(texts)
            # print(sums_texts)
            # print(proximity)
            # print(index)

        except Exception as err:
            print(f"Houve um erro na busca na wikipedia!\nERRO: {err}")

        finally:
            if min_difference < 200:
                return texts[index]
            return ""


if __name__ == "__main__":
    w = Wiki()
    code, res, look, link = w.research("Nikola")
    print(res)
