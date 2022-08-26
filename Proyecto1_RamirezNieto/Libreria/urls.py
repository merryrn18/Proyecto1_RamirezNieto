from django.urls import path
from  Libreria.views import inicio,libros,addLibros,searchLibros,revistas,addRevistas,searchRevistas,audios,addAudios,searchAudios

urlpatterns = [
    path('', inicio, name="LibreriaInicio"),
    path('libros', libros,name="LibreriaLibros"),
    path('addLibros', addLibros,name="LibreriaAddLibros"),
    path('searchLibros', searchLibros,name="LibreriaSearchLibros"),
    path('revistas', revistas,name="LibreriaRevistas"),
    path('addRevistas', addRevistas,name="LibreriaAddRevistas"),
    path('searchRevistas', searchRevistas,name="LibreriaSearchRevistas"),
    path('audios', audios,name="LibreriaAudios"),
    path('addLibros', addAudios,name="LibreriaAddAudios"),
    path('searchAudios', searchAudios,name="LibreriaSearchAudios"),
    
]