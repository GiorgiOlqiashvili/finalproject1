from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import BookViewSet, AuthorViewSet, GenreViewSet, ConditionViewSet, BookRequestViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Book Lending Service API",
        default_version='v1',
        description="API documentation for the Book Lending Service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)
router.register('conditions', ConditionViewSet)
router.register('requests', BookRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # Keep this for authentication
    path('auth/token/', include('djoser.urls.authtoken')),  # Correct path for token authentication
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
