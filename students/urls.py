from django.urls import path, include
from . import views

urlpatterns = [
    path('', view= views.index),
    path('<int:id>/', view= views.index),
    path('categories/', views.getAllCategories),
    path('create/', view= views.createStudent),
    path('send-mail/', view= views.sendMail)
]

urlpatterns.append(path('basic/', include([
    path('', view= views.getAll),
    path('<int:id>/', view= views.getById),
    path('create/', view= views.create),
    path('<int:id>/update/', view= views.update),
    path('<int:id>/delete/', view= views.delete)
])))


