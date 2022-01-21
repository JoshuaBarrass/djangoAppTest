from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # this urls.py holds urls that come after '.com/polls/'
    path('', views.IndexView.as_view() , name='index'),
    # for '.com/polls/<int: questionId>/'
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # for '.com/polls/<int: questionId>/results/'
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),       # using pk instead of questionId for use in the generic views in views.py, the vote doesnt use these therefore uses questionId
    # for '.com/polls/<int: questionId>/vote/'
    path('<int:questionId>/vote/', views.vote, name='vote'),    
    
]
