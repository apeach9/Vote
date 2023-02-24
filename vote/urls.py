from django.urls import path
from vote import views

app_name = 'vote'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail' ),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
    path('<int:question_id>/vote/result/', views.result, name = 'result'),
]