
from django.shortcuts import render , redirect , HttpResponseRedirect
from BillieJeansStart.models.product import Product
from BillieJeansStart.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1


        request.session['cart']= cart
        print('cart', request.session['cart'])
        return redirect('homepage')





    def get(self,request):
        products = None

        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are :   ', request.session.get('email'))

        return render(request, 'BillieJeansStart/HomePage.html', data)








def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def Store(request):
    return render(request, 'Store.html')

def Logout(request):
    return render(request, 'Logout.html')

