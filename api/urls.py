from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mealplan API",
        default_version='v1',
        description="API for mealplan app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mikkel.skagen@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'units', views.UnitOfMeasurementViewSet)
router.register(r'mealplans', views.MealPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
