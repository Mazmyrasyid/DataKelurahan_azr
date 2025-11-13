# warga/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet # Pastikan Anda mengimpor ViewSet

# --- INISIALISASI ROUTER ---

# 1. Buat sebuah router
router = DefaultRouter()

# 2. Daftarkan ViewSet untuk Warga (Menggantikan 2 baris path() lama)
router.register(r'warga', WargaViewSet, basename='warga')

# 3. Daftarkan ViewSet untuk Pengaduan (Menyelesaikan tugas praktikum)
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

# --- DEFINISI URL ---

# URL API sekarang ditentukan secara otomatis oleh router.
# path('', include(router.urls)) akan menghasilkan 4 URL endpoint untuk setiap ViewSet
urlpatterns = [
    # Baris ini secara otomatis mencakup semua URL yang dibuat oleh router
    path('', include(router.urls)), 
]