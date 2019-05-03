from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questao, Participante, Opcao


def index(request):
    return HttpResponse("Olá, esta é a página inicial de SGBE-MySQL do grupo 4 constituído pelos alunos 21410 e 21386.")


def detalhes(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'mysqlapp/detalhes.html', {'questao': questao})


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'mysqlapp/resultados.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_escolhida = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'mysqlapp/detalhes.html', {'questao': questao,'error_message': "Não escolheu uma opção.",})
    else:
        participante = Participante(nome=request.POST['nome'], email=request.POST['email'])
        participante.opcao = opcao_escolhida
        participante.save()
        opcao_escolhida.votos += 1
        opcao_escolhida.save()
        return HttpResponseRedirect(reverse('mysqlapp:resultados', args=(questao.id,)))


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

    lista_participantes = Participante.objects.order_by('-id')[:5]
    lista_combinada = []

    for participante in lista_participantes:
        opcao = str(Opcao.objects.filter(id=participante.opcao_id)[0])
        lista_combinada.append(participante.nome + ' votou em ' + opcao)

    print(lista_combinada)
    contexto = {'lista_combinada': lista_combinada}
    return render(request, 'mysqlapp/participantes5.html', contexto)
