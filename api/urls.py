from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()

router.register('v1/employee',views.EmployeeView,basename='emplyoyee')

urlpatterns = [
    
]+router.urls