from django.shortcuts import render
import random as rd

# Create your views here.

def cart_detail(request):
    
    return render(request,'cart_detail.html')

def cart_detail_example(request):
    if request.session.get("cart"):

        # 1. We only can put json or serializable obj
        # 2. the session obj only save when you modify session
        """
            if you do :
                request.session['cart']['a'] = rd.randint(0,1)
                request.modified -> False

                request.session['cart']['a'] = {}
                request.modified -> True

            or write code 
                request.session['cart']['a'] = rd.randint(0,1)
                AND....
                request.modified = True


        """
        request.session['cart'] = rd.randint(0,1)

    return render(request,'cart_detail.html')