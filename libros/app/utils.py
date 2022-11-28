import json
from .models import *

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		carrito = json.loads(request.COOKIES['carrito'])
	except:
		carrito = {}
		print('CART:', carrito)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in carrito:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:	
			if(carrito[i]['quantity']>0): #items with negative quantity = lot of freebies  
				cartItems += carrito[i]['quantity']

				product = Libro.objects.get(id=i)
				total = (product.precio * carrito[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += carrito[i]['quantity']

				item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.nombre, 'price':product.precio, 
				'imageURL':product.imageURL}, 'quantity':carrito[i]['quantity'],
				}
				items.append(item)

				
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Libro.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
		)
	return customer, order

