from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Tarefa
from .forms import TarefaForm 
from django.contrib import messages

# Create your views here.


def home(request):

    search = request.GET.get('search')

    if search:
        tarefas = Tarefa.objects.filter(title__icontains = search)
    else:
        lista_tarefas = Tarefa.objects.all().order_by('-creat_at')

        paginator = Paginator(lista_tarefas, 5)

        page = request.GET.get('page')

        tarefas = paginator.get_page(page)

    return render(request, 'home/index.html', {'tarefas': tarefas})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tarefa/tarefa.html', {'tarefa': tarefa})

def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit = False)
            tarefa.done = 'doing'
            tarefa.save()
            return redirect('/')
    else:
        form = TarefaForm()
        return render(request, 'tarefa/novatarefa.html', {'form': form})
    
def editar (request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TarefaForm(instance = tarefa)

    if (request.method == "POST"):
        form = TarefaForm(request.POST, instance = tarefa)

        if (form.is_valid()):
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tarefa/editar.html', {'form': form, 'tarefa': tarefa})    

    else:
        return render(request, 'tarefa/editar.html', {'form': form, 'tarefa': tarefa})
    

def deletar(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()

    messages.info(request, "Tarefa deletada com sucesso")

    return redirect('/')

