class Carrito:
    
    total = 0

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
            
        else:
            self.carrito = carrito

    def agregar(self, libro):
        id = str(libro.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "libro_id": libro.id,
                "nombre": libro.nombre,
                "acumulado": libro.precio,
                "cantidad": 1,
                "valor_libro" : libro.precio
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += libro.precio
            self.carrito[id]["valor_libro"] = libro.precio
        self.total += self.carrito[id]['acumulado']
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, libro):
        id = str(libro.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, libro):
        id = str(libro.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= libro.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(libro)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    def cantidad(self):
        cantidad = self.carrito[id]["cantidad"]
        valor_libro = self.carrito[id]["valor_libro"]

    def sumarTotal(self):
        for key, value in self.carrito.items:
            total = value.acumulado
            print(total)

