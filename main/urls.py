from django.urls import path

from main.views import TaskViewSet, TaskListViewSet

urlpatterns = [
    path('task', TaskViewSet.as_view({'get': 'list'}), name='tasks'),
    path('task/<int:pk>', TaskViewSet.as_view({'get', 'retrieve'}), name='task'),

    path('task-list', TaskListViewSet.as_view({'get': 'list'}), name='task-lists'),
    path('task-list/<int:pk>', TaskListViewSet.as_view({'get': 'retrieve'}), name='task-list'),
]