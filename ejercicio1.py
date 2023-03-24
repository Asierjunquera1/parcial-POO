class Libro:
    def __init__(self, titulo, autor, año_publicacion, numero_paginas, editorial):
        self.titulo=titulo
        self.autor=autor
        self.año_publicacion=año_publicacion
        self.numero_paginas=numero_paginas
        self.editorial=editorial
    
    def describir(self):
        print("El titulo del libro es:", self.titulo)
        print("El autor del libro es:", self.autor)
        print("El año de publicación del libro es:", self.año_publicacion)
        print("El número de páginas del libro es:", self.numero_paginas)
        print("La editorial del libro es:", self.editorial)

    