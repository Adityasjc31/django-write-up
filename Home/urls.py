from django.urls import path
from Home.views import *

urlpatterns = [
    path('',Home,name="home"),
    path('logout',logout,name="logout"),  # type: ignore
    # path('img',ImgUploadTest,name="img"),
    # path('dHd',dataHelpDisplay,name="dHd"),
    # path('tin',txtInput,name="tin"),
    # path('ts',txtSave,name="ts"),
    # path('upload',getData,name="upload"),
]