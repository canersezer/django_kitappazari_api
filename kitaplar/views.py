from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.validators import ValidationError

from .serializer import KitapSerializer,YorumSerializer
from .models import  Kitap,Yorum
from .permissions import IsAdminUserOrReadOnly




class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes=[IsAdminUserOrReadOnly]
 
class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes=[IsAdminUserOrReadOnly]


class YorumCreateApiView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer


    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap,yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError('Bir kullanici bir kitaba bir yorum yapabilir')
        serializer.save(kitap=kitap,yorum_sahibi=kullanici)
class YorumDeteilApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
