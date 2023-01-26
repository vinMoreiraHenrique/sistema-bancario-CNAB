from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import form_transactions
from .models import FileModel
import datetime


def home(request):
    form = form_transactions()
    return render(request, "home.html", {"form": form})


def form_processing(request):
    return HttpResponse("test")


def save_file_content(request):
    if request.method == "POST":
        form = form_transactions(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            for chunk in file.chunks():
                for line in chunk.decode().splitlines():
                    tipo = line[:1]
                    data = datetime.datetime.strptime(str(line[1:9]), "%Y%m%d").date()
                    valor = line[9:19]
                    cpf = line[19:30]
                    cartao = line[30:42]
                    hora = line[42:48]
                    dono_da_loja = line[48:62]
                    nome_da_loja = line[62:81]
                    saved_file = FileModel(
                        tipo=tipo,
                        data=data,
                        valor=valor,
                        cpf=cpf,
                        cartao=cartao,
                        hora=hora,
                        dono_da_loja=dono_da_loja,
                        nome_da_loja=nome_da_loja,
                    )
                    saved_file.save()

    else:
        form = form_transactions()
    return render(request, "home.html", {"form": form})
