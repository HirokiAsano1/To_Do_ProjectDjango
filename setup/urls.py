
from django.contrib import admin
from django.urls import path
from To_do.views import TodoListView,TodoCreateView,TodoUpdateView,TodoDeleteView,TodoCompleteView;
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",TodoListView.as_view(), name = "todo_list"),
    path("create",TodoCreateView.as_view(),name = "todo_create"),
    path("update/<int:pk>",TodoUpdateView.as_view(), name="todo_update"), #e prciso passra o int:pk , pois o programa precisa do id para pegar o id especifico do objeto
    path("delete/<int:pk>",TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>",TodoCompleteView.as_view(), name="todo_complete")
]
