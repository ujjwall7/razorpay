from django.shortcuts import render,HttpResponse
import razorpay
from . models import *
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        print(name , amount)
        client = razorpay.Client(auth =("rzp_test_zn5vX1Gd2iuRqu" , "cchtb0rOteE627IDxuTYrOn3"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1' })
        coffee = Coffee(name = name , amount = amount , order_id = payment['id'])
        coffee.save()
        return render(request, 'index.html' ,{'payment':payment})
    return render(request, "index.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a =  (request.POST)    #jo bhi razor pay ne bheja hoga post karke vo a ke andar store kar lenge
        order_id = ""
        for key , item in a.items():
            if key == "razorpay_order_id":
                order_id = item
                break
        user = Coffee.objects.filter(order_id = order_id).first()
        user.paid = True
        user.save()
    return render(request, "success.html")

