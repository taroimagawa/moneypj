from django.contrib import admin
from django.urls import path
from money.views import MoneyListView, MoneyDetailView, MoneyCreateView, MoneyUpdateView, MoneyDeleteView

urlpatterns = [
    path('', MoneyListView.as_view(), name='list'),
    path('detail/<int:pk>', MoneyDetailView.as_view(),name='detail'),
    path('create/', MoneyCreateView.as_view(), name='create'),
    path('update/<int:pk>', MoneyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MoneyDeleteView.as_view(), name='delete'),
    path('admin/', admin.site.urls),
]

