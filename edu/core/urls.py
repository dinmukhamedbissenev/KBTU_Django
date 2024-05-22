from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, CourseViewSet, ModuleViewSet, AssignmentViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('assignment/<int:assignment_id>/', views.grade_assignment, name='grade_assignment'),
    path('assignment_details/<int:assignment_id>', views.assignment_details, name='assignment_details'),
    path('assignment/', views.assignment),
    path('category/', views.category),
    path('course/', views.course)

]