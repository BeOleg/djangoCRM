from .models import Lead
from rest_framework import serializers

class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = Lead
		fields = ('first_name', 'last_name', 'phone',)