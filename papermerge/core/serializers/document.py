from rest_framework_json_api import serializers

from papermerge.core.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        resource_name = 'documents'
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at'
        )
