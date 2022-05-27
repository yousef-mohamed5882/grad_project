from django.urls import include, path
from . import api
from . import views

app_name = 'Q_A'
urlpatterns = [
    path('api/question-list',api.questionlistapi,name = 'questionlistapi'),
    path('api/results',api.results_api,name = 'results'),
    path('',views.function2)
]