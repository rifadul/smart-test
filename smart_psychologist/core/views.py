from django.shortcuts import render
from django.views import View
from ecoshop.models import Cart

# Create your views here.


def home(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'core/home.html',{'total_item':cart})


# class ContactView(View):
#     def get(self,request):
#         form = ContactForm()
#         return render(request,request,'core/contact.html',{'form':form})






# def contact(request):
#     if request.method == "POST":
#         forms = ContactForm(request.POST)
#         if forms.is_valid():
#             messages.success(request,'Message Sent Successfully')
#             forms.save()
#             forms = ContactForm()
#     else:
#         forms = ContactForm()
#     return render(request,'core/contact.html',{'forms':forms})