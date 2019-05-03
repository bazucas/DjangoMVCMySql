from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Questao, Participante, Opcao


def index(request):
    return HttpResponse("Olá, esta é a página inicial de SGBE-MySQL do grupo 4 constituído pelos alunos 21410 e 21386.")


def detalhes(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'mysqlapp/detalhes.html', {'questao': questao})


def resultados(request, questao_id):
    response = "Está a ver os resultados da questão %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Está a votar na questão %s." % questao_id)


def aluno(request, participante_id):
    return HttpResponse("A aluna %s chama-se Ana Silva." % participante_id)


def aluno1234(request):
    return HttpResponse("A aluna 1234 chama-se Maria Pereira.")


def aluno2345(request):
    return HttpResponse("O aluno 2345 chama-se Pedro Monteiro.")


def aluno3456(request):
    return HttpResponse("A aluna 3456 chama-se Ana Silva.")


def ultimas5(request):
    lista_ultimas_questoes = Questao.objects.order_by('-data_pub')[:5]
    contexto = {'lista_ultimas_questoes': lista_ultimas_questoes}
    return render(request, 'mysqlapp/ultimas5.html', contexto)


def participantes5(request):
    # a = Participante(id=1, nome='Luis Inacio', email='luis@luis.pt', opcao_id=1)
    # a.save()
    # b = Participante(id=2, nome='Miguel Silva', email='miguel@miguel.pt', opcao_id=2)
    # b.save()
    # c = Participante(id=3, nome='Jose Carvalho', email='jose@jose.pt', opcao_id=3)
    # c.save()
    # d = Participante(id=4, nome='Alex Torres', email='alex@alex.pt', opcao_id=4)
    # d.save()
    # e = Participante(id=5, nome='Ruben Santos', email='ruben@ruben.pt', opcao_id=5)
    # e.save()

    lista_participantes = Participante.objects.all()
    lista_combinada = []

    for participante in lista_participantes:
        opcao = str(Opcao.objects.filter(id=participante.opcao_id)[0])
        lista_combinada.append(participante.nome + ' votou em ' + opcao)

    print(lista_combinada)
    contexto = {'lista_combinada': lista_combinada}
    return render(request, 'mysqlapp/participantes5.html', contexto)
