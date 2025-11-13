# warga/serializers.py

from rest_framework import serializers
from .models import Warga, Pengaduan # Pastikan Pengaduan sudah diimpor

## Serializer untuk Model Warga (sudah ada)
class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

## Serializer untuk Model Pengaduan (kode yang Anda tambahkan)
class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        # Tentukan field dari model Pengaduan yang ingin kita ekspos di API
        fields = ['id', 'judul', 'isi', 'status', 'tanggal_pengaduan', 'pelapor']