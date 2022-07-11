from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:home")


class TaskDeleteView(generic.DeleteView):
    template_name = "todo_list/task_confirm_delete.html"
    model = Task
    success_url = reverse_lazy("todo_list:home")


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    if not task.is_done:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:home"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    template_name = "todo_list/tag_confirm_delete.html"
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
