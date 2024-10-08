from django.urls import path
from django.conf import settings
from .views import CustomLoginView, SignUpView, edit_profile, logout_view
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('logout/', logout_view, name='logout'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('cancel-workshop/<int:workshop_id>/', views.cancel_workshop, name='cancel_workshop'),  # Use cancel_workshop directly
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
