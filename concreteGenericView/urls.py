"""
URL configuration for concreteGenericView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from book import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.StudentList.as_view()),
    path('create/',views.StudentCreate.as_view()),
    path('update/<int:pk>/',views.StudentUpdate.as_view()),
    path('retrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('delete/<int:pk>/',views.StudentDelete.as_view()),
    path('lc/',views.Studentlc.as_view()),
    path('rup/<int:pk>/',views.Studentrup.as_view()),
    path('rd/<int:pk>/',views.StudentRD.as_view()),
    path('rud/<int:pk>/',views.StudentRUD.as_view()),
    path('', include(router.urls)),


]



