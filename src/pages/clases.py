class Tienda_discos:
    def __init__(self, band, album, year):
        self.band = band
        self.album = album
        self.year = year

    def print_attributes(self):
        print("Banda:", self.band)
        print("Álbum:", self.album)
        print("Año:", self.year)


class Coleccion_Tienda(Tienda_discos):
    def __init__(self, band, album, year, stock):
        self.band = band
        self.album = album
        self.year = year
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def print_stock(self):
        print("Stock disponible:", self.stock)


disco_base = Tienda_discos("Blink 182", "One More Time", 2023)
disco_base.print_attributes()

disco_coleccion = Coleccion_Tienda("Sum 41", "Underclass Hero", 2007, 4)
disco_coleccion.print_attributes()
disco_coleccion.print_stock()