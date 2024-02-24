from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from common.context_processor import Lenguage
from common.form import FormCreate
from common.models import About, Products, Testimonial, ClinicMember, Services, Contacts, ApplicationForm, Banners
from django.contrib import messages


# Create your views here.


def home(request, *args, **kwargs):
    language = request.COOKIES.get('django_language')
    res = []
    about = About.objects.all()
    product = Products.objects.all()
    b = Banners.objects.all()
    t = Testimonial.objects.all()
    m = ClinicMember.objects.all()
    s = Services.objects.all()
    c = Contacts.objects.all()
    d = {}

    if language == Lenguage.Russion:
        a = About.objects.values('title_ru', 'description_ru', ).first()
        d['about_title'] = a["title_ru"]
        d['about_description'] = a["description_ru"]

        res.append(d)

    elif language == Lenguage.Uzbek:
        a = About.objects.values('title_uz', 'description_uz', ).first()

        d['about_title'] = a["title_uz"]
        d['about_description'] = a["description_uz"]

        res.append(d)

    elif language == Lenguage.English:
        a = About.objects.values('title_en', 'description_en', ).first()

        d['about_title'] = a["title_en"]
        d['about_description'] = a["description_en"]

        res.append(d)

    return render(request, 'index.html', context={"about_text": res, "about_list": about, "products": product
        , "testimonials": t, "members": m, "services": s, 'contact': c, 'banner': b, })


def form_create(request):
    if request.method == 'POST':
        form = FormCreate(request.POST)
        if form.is_valid():
            if request.POST.get('id') is not None:
                id__ = request.POST.get('id')
                ApplicationForm.objects.create(product_id=id__, **form.cleaned_data)
                if request.LANGUAGE_CODE == 'uz':
                    messages.success(request, "Muffaqiyatli Xabaringiz Yuborildi!")
                elif request.LANGUAGE_CODE == 'ru':
                    messages.success(request, "Ваше сообщение было успешно отправлено!")
                else:
                    messages.success(request, "Your message has been successfully sent!")
                return redirect('index')
            ApplicationForm.objects.create(**form.cleaned_data)
            if request.LANGUAGE_CODE == 'uz':
                messages.success(request, "Muffaqiyatli Xabaringiz Yuborildi!")
            elif request.LANGUAGE_CODE == 'ru':
                messages.success(request, "Ваше сообщение было успешно отправлено!")
            else:
                messages.success(request, "Your message has been successfully sent!")
            return redirect('index')


        else:
            messages.error(request, form.errors)
    return redirect('index')


def page_not_found_view(request, exception=None):
    return render(request, '404.html', status=404)
