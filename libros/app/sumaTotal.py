def sumaTotal(request):
    total = 0 
    print("total\n---> ",total)
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key,value in request.session["carrito"]:
                total += int(value["acumulado"])
    return {"total":total}
