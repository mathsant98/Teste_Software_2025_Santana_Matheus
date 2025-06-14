import myapplication as tum

class TestBlogger:
    @classmethod
    def setup_class(cls):
        cls.user = "alice"
        cls.b = tum.Blogger(cls.user)
        print("This should be printed, but it won't be!")

    def test_inherit(self):
        posts = [1, 2, 3]
        assert issubclass(tum.Blogger, tum.Site)  # Você está testando se tum.Blogger (que é uma classe definida como class Blogger(Site)) é uma subclasse de str. Isso não é verdade, então o assert falha — exatamente como você queria para testar a saída de print() capturada.
        links = self.b.get_links(posts)
        print(len(links))  # Também não aparecerá sem -s
