from django.shortcuts import render

from main.models import Settings
from main.views import not_authenticated

from . import forms
from . import utils

# Create your views here.

DEF_VARIATE = 5
DEF_INITIAL = {"size": forms.DalleForm.SIZES[2], "amount": 1}


def ai_page(request):
    if not request.user.is_authenticated:
        return not_authenticated(request)
    
    if request.method == "POST":
        form = forms.DalleForm(request.POST)
        print(f"\n\n\n{form.data} {form.is_valid()}\n\n\n")
        
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]
            amount = form.cleaned_data["amount"]
            size = form.cleaned_data["size"]
            
            key = Settings.objects.get(user=request.user).openai_key
            context = {"form": form,
                       "generated": utils.get_generated_imgs(key, prompt, amount, size),
                       "prompt": prompt,
                       "amount": amount,
                       "size": size,
                       }
            
            if "gallery" in form.cleaned_data:
                context["gallery"] = form.cleaned_data["gallery"]
            
            return render(request=request, template_name="ai_page.html", context=context)
    
    context = {"form": forms.DalleForm(DEF_INITIAL)}
    
    saved_imgs = utils.get_saved_imgs()
    if saved_imgs:
        context["gallery"] = saved_imgs
    
    return render(request=request, template_name="ai_page.html", context=context)


def variate(request, url, prompt, size, amount):
    if not request.user.is_authenticated:
        return not_authenticated(request)

    key = Settings.objects.get(user=request.user).openai_key
    initial = {"prompt": prompt, "size": size, "amount": amount}
    context = {"generated": utils.variate_image(key, url, DEF_VARIATE),
               "form": forms.DalleForm(initial=initial)}
    context.update(initial)
    return render(request=request, template_name="ai_page.html", context=context)


def save_page(request, url, prompt, size):
    if not request.user.is_authenticated:
        return not_authenticated(request)
    
    return render(request=request, template_name="save.html",
                  context={"url": url, "prompt": prompt, "size": size})


def resolution_page(request, url, prompt, size):
    if not request.user.is_authenticated:
        return not_authenticated(request)
    
    return render(request=request, template_name="resolution.html",
                  context={"result": utils.increase_image_resolution(url), "prompt": prompt, "size": size})


def gallery_page(request):
    if not request.user.is_authenticated:
        return not_authenticated(request)
    
    context = {"message": "Not ready yet. But magic is coming..."}
    return render(request=request, template_name="gallery_page.html", context=context)


def image_page(request, pk):
    if not request.user.is_authenticated:
        return not_authenticated(request)
    
    if pk > 100:
        context = {"message": "404. Not Found"}
    else:
        context = {"message": "Magic things happens here.."}
    
    return render(request=request, template_name="image_page.html", context=context)
