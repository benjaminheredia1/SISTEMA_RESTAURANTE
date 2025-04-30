class Pedidos():
    def __init__(self):
        self.__pedidos = []
        self.__total = 0
        
    def add_pedido(self, Pedidos = {'valor': 0, 'platos': []}):
        self.__pedidos.append(Pedidos)
    def cuenta(self): 
        for pedido in self.__pedidos:
            self.__total += pedido['valor']
        return self.__total
    def factura(self):
        print("+" + "=" * 50 + "+")
        print("|{:^50}|".format("FACTURA"))
        print("+" + "=" * 50 + "+")
        for i, pedido in enumerate(self.__pedidos, start=1):
            print("| Pedido {:<42} |".format(i))
            print("| {:<48} |".format("Platos:"))
            for plato in pedido['platos']:
                print("|   - {:<45} |".format(plato))
            print("| {:<48} |".format(f"Valor: ${pedido['valor']:.2f}"))
            print("+" + "-" * 50 + "+")
        print("| {:<48} |".format(f"TOTAL: ${self.cuenta():.2f}"))
        print("+" + "=" * 50 + "+")
    def editarPedido(self): 
        while True:
            for i in range(len(self.__pedidos)):
                print("Pedido: ",  self.__pedidos[i])
                print("Platos: ", self.__pedidos[i]['platos'])
                print("Valor: ", self.__pedidos[i]['valor'])
                print("¿Desea editar este pedido? (s/n)")
                respuesta = input()
                if(respuesta.lower() == "si"):
                    print("¿Qué desea editar? (platos/valor)")
                    respuesta = input()
                    if(respuesta.lower() == 'platos'):
                        print("¿Qué plato desea agregar?")
                        platos = input()
                        self.__pedidos[i]['platos'].append(platos)  
                    elif(respuesta.lower() == 'valor'):
                        print("¿Qué valor desea agregar?")
                        valor = input()
                        self.__pedidos[i]['valor'] += float(valor)
if  __name__ == "__main__":

    pedidos = Pedidos()
    pedidos.add_pedido({'valor': 100, 'platos': ['pizza', 'ensalada']})
    pedidos.add_pedido({'valor': 200, 'platos': ['pasta', 'sopa']})   
    pedidos.factura()
    pedidos.editarPedido()
    pedidos.factura()