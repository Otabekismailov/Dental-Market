from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from common.context_processor import Lenguage
from common.form import FormCreate
from common.models import About, Products, Testimonial, ClinicMember, Partners, Contacts, ApplicationForm, Banners, \
    Category
from django.contrib import messages

# Create your views here.


def home(request, *args, **kwargs):
    language = request.COOKIES.get('django_language')

    about = About.objects.all()
    product = Products.objects.all()
    b = Banners.objects.all()
    t = Testimonial.objects.all()
    m = ClinicMember.objects.all()
    s = Partners.objects.all()
    c = Contacts.objects.all()
    category_list = Category.objects.all()

    return render(request, 'index.html', context={"about_list": about, "products": product
        , "testimonials": t, "members": m, "services": s, 'contact': c, 'banner': b,"category": category_list })


def form_create(request):
    if request.method == 'POST':
        form = FormCreate(request.POST)
        if form.is_valid():
            if request.POST.get('id') is not None:
                id__ = request.POST.get('id')
                ApplicationForm.objects.create(category_id=id__, **form.cleaned_data)
                if request.LANGUAGE_CODE == 'uz':
                    return JsonResponse(
                        {"message": "So'rovingiz uchun raxmat. Tez orada biz siz bilan bog'lanamiz!", "status": True})
                elif request.LANGUAGE_CODE == 'ru':
                    return JsonResponse(
                        {"message": "Спасибо за ваш запрос. Мы свяжемся с вами в ближайшее время!", "status": True})
                else:
                    return JsonResponse(
                        {"message": "Thank you for your inquiry. We will contact you shortly!", "status": True})

            ApplicationForm.objects.create(**form.cleaned_data)
            if request.LANGUAGE_CODE == 'uz':
                return JsonResponse(
                    {"message": "So'rovingiz uchun raxmat. Tez orada biz siz bilan bog'lanamiz!", "status": True})
            elif request.LANGUAGE_CODE == 'ru':
                return JsonResponse(
                    {"message": "Спасибо за ваш запрос. Мы свяжемся с вами в ближайшее время!", "status": True})
            else:
                return JsonResponse(
                    {"message": "Thank you for your inquiry. We will contact you shortly!", "status": True})
        else:
            res = []
            for key, value in form.errors.items():
                res.append({"field": key, "error": value[0]})
            return JsonResponse({"message": res, "status": False})
    return redirect('index')


def page_not_found_view(request, exception=None):
    return render(request, '404.html', status=404)
