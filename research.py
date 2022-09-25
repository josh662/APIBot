from googlesearch import search


class Websearch:
    def __init__(self):
        pass

    def get_links(self, text, websites_number=5):
        self.text = text
        self.websites_number = websites_number
        ok = True

        links_result = []
        videos_result = []
        res = []

        links_current = 0
        videos_current = 0

        max_researchs = 50
        try:
            for result in search(f'"{self.text}" google', stop=max_researchs):
                check = self.check_exceptions(result)
                if check:
                    links_result.append(result)
                    links_current += 1

                    if links_current >= self.websites_number:
                        break

            for result in search(f'"{self.text}" youtube', stop=max_researchs):
                if "youtube" in result:
                    videos_result.append(result)
                    videos_current += 1

                    if videos_current > 5:
                        break

            res = [links_result, videos_result]
        except Exception as err:
            print(f"Erro na Pesquisa !!!\nERRO: {err}")
            ok = False
            res = []

        finally:
            return ok, res

    def check_exceptions(self, url):
        add = True
        self.exceptions = [
            "youtube",
            "amazon",
            "pinterest",
            "cafepress",
            "themebeta",
            "teslamotorsclub"
        ]

        for exception in self.exceptions:
            if exception in url:
                add = False
        return add


if __name__ == "__main__":
    web = Websearch()
    res = web.get_links("Quem foi Albert Einstein")
    # print(res[1])
