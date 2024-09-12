from .models import To_do
from django.views.generic import ListView , CreateView , UpdateView,DeleteView,View
from django.urls import reverse_lazy #responsavel de pegar o nome da url e retornar  a rota completa
from django.shortcuts import get_object_or_404,redirect
from datetime import date

# Create your views here.

class TodoListView(ListView): #class based view (cbv)
    model = To_do #renderiza os elemtnos na tabela To_Do
    template_name = 'To_do/todo_list.html'
    context_object_name = 'to_do_list'  # Define o nome da variável no template
    

class TodoCreateView(CreateView):
    model = To_do #renderiza os elemtnos na tabela To_Do
    template_name = 'To_do/todo_form.html'
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list") #quando a ação for finalizada do post , o usuario é redirecionado para a pagina descrita

class TodoUpdateView(UpdateView):
    model = To_do 
    template_name = 'To_do/todo_form.html'
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list") 

class TodoDeleteView(DeleteView):
    model = To_do 
    template_name = 'To_do/todo_confirm_delete.html'
    success_url = reverse_lazy("todo_list") 

class TodoCompleteView(View):
    def get(self,request,pk):
        todo = get_object_or_404(To_do,pk=pk)#buscar no banco de dados que tenha a coluna pk igual a que a aplicação recebe
        todo.mark_has_complete()
        return redirect("todo_list")#redirecionando para essa pagina

