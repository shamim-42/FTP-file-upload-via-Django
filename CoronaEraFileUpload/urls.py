
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file-upload/', include('apps.fileUpload.urls'))
]


# if settings.DEBUG:

#     # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
#     urlpatterns += static(
#         settings.STATIC_URL,
#         document_root=settings.STATIC_ROOT
#     )
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )
