from . views import TeamsApiView, TeammatesApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'teams', TeamsApiView, basename='team')
router.register(r'teammates', TeammatesApiView, basename='teammate')

app_name = 'api'

urlpatterns = [
    # path('teams/', TeamsListApiView.as_view()),
    # path('teams/<int:pk>', TeamsInstanceApiView.as_view()),
    # path('teammates/', TeammatesListApiView.as_view()),
    # path('teammates/<int:pk>', TeammatesInstanceApiView.as_view()),
]

urlpatterns.extend(router.urls)
