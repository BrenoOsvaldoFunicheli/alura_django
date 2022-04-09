from django.urls import path, include


from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout"),
    path('criar_receita/', views.criar_receita, name="criar_receita"),
    path('deleta_receita/<int:receita_id>', views.deleta_receita, name="deleta_receita"),
]