from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('exams', views.ExamView)
router.register('users', views.UserView)
router.register('results', views.ResultView)

urlpatterns = [
    path('', include(router.urls))
]
