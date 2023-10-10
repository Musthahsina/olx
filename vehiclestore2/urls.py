from django.urls import path
from vehiclestore2.views import SignUpView,SignInView,IndexView,VehicleCreateView,VehicleListView,VehicleDetailView,VehicleUpdateView,remove_vehicle



urlpatterns=[
    path("signup",SignUpView.as_view(),name="signup"),
    path("signin",SignInView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="index"),
    path("add/",VehicleCreateView.as_view(),name="add-vehicle"),
    path("all/",VehicleListView.as_view(),name="list-vehicle"),
    path("<int:pk>/",VehicleDetailView.as_view(),name="detail-vehicle"),
    path("<int:pk>/change",VehicleUpdateView.as_view(),name="change-vehicle"),
    path("<int:pk>/remove",remove_vehicle,name="remove-vehicle"),





]