from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Form_transactions
from .models import FileModel
import datetime
from django.views import View
from django.db.models import Sum, When, Case, F


def home(request):
    form = Form_transactions()
    return render(request, "home.html", {"form": form})


def form_processing(request):
    return HttpResponse("test")


def get_from_database(request):
    if request.method == "GET":
        Form_transactions.objects.all()


def save_file_content(request):
    if request.method == "POST":
        form = Form_transactions(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            for chunk in file.chunks():
                for line in chunk.decode().splitlines():
                    tipo = line[:1]
                    data = datetime.datetime.strptime(str(line[1:9]), "%Y%m%d").date()
                    valor = int(line[9:19]) / 100
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
        form = Form_transactions()
    return render(request, "home.html", {"form": form})


def list_stores_saldo(request):
    store_saldo = (
        FileModel.objects.values("nome_da_loja")
        .annotate(
            total_saldo=Sum(
                Case(
                    When(tipo__in=[2, 3, 9], then=-F("valor")),
                    default=F("valor"),
                )
            )
        )
        .distinct()
    )

    return render(request, "store_saldo.html", {"store_saldo": store_saldo})
