from django.shortcuts import render
import googletrans
from googletrans import Translator
# Create your views here.
def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if request.method == "POST":
        b = request.POST.get("bf")
        f = request.POST.get("fr")
        t = request.POST.get("to")
        translator = Translator()
        a = translator.translate(b, src=f, dest=t)
        context.update({
            "bf" : b,
            "af" : a.text,
            "fr" : f,
            "to" : t
        })


    return render(request, "trans/index.html", context)