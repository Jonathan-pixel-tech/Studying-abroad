from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('universidades/', views.listaUniversidades.as_view(), name='universidades'),
    path('universidades/<int:pk>', views.detalha, name='detalha'),
    path('pais/<int:pk>', views.mostra_pais, name='mostra_pais'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/usuario', views.cadastraCollege.as_view(), name='dashboard_usuario'),
    path('dashboard/collegeList', views.listaCollege.as_view(), name='collegeList'),
    path('dashboard/excluir/<int:pk>', views.DeletaUniversidade.as_view(), name='deleta'),

]