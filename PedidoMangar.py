class Pedidos():
    def __init__(self):
        self.pedidos = []
        self.total = 0
        
    def add_pedido(self, Pedidos = {valor: 0, platos: []}):
        self.pedidos.push(Pedidos)
    def cuenta(self): 
        for pedido in self.pedidos:
            self.total += pedido['valor']
        return self.total
    

    
if  __name__ == "__main__":
   Pedidos = Pedidos()