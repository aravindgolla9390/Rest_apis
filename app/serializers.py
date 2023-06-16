from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):
   class Meta:
      fields='__all__'
      model=Book