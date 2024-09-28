from rest_framework import serializers # type: ignore
from .models import Postlist


class PostlistSerializer(serializers.ModelSerializer):
	class Meta:
		model=Postlist
		fields=('post_id','id','title','content','created_at', 'updated_at')