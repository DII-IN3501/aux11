from django.shortcuts import render
from mainApp.models import Pizza, Pedido, Carrito

def index(request):
    context = {"pizzas": Pizza.objects.all()}
    return render(request, 'mainApp/index.html', context)

def pedir(request):
    pedido = Pedido(cliente=request.user.cliente)
    pedido.save()

    for k in request.POST:
        if k.startswith('pizza-'):
            pizza_id = int(k[6:]) # Extraemos solo el número de pizza-n y lo convertimos a entero. Ej: "pizza-4" -> 4
            cantidad = int(request.POST[k]) # Convertimos a entero esta cantidad
            tamano = request.POST["tamano-"+str(pizza_id)] # Extraemos el tamaño de la pizza por su ID.

            carrito = Carrito(pedido=pedido,
                              pizza=Pizza.objects.get(id=pizza_id),
                              cantidad=cantidad,
                              tamano=tamano)
            carrito.save()

    #context = {"pizzas": Pizza.objects.all()}
    #return render(request, 'mainApp/index.html', context)
    return index(request)

def pedidos(request):
    listapedidos = Pedido.objects.filter(cliente=request.user.cliente)

    context = {"pedidos": listapedidos}
    return render(request, 'mainApp/pedidos.html', context)
