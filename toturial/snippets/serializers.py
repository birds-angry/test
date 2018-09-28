from rest_framework import serializers
from .models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     stycle = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
#
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.linenos = validated_data.get('linenos',instance.linenos)
#         instance.language = validated_data.get('language',instance.language)
#         instance.stycle = validated_data.get('stycle',instance.stycle)
#         instance.save()
#         return instance

# 使用ModelSerializer
# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
#
#     class Meta:
#         model = Snippet
#         fields = ('url', 'id', 'highlight', 'owner',
#                   'title', 'code', 'linenos', 'language', 'stycle')
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'snippets')

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = '__all__'



class Customfield(serializers.Field):
    default_error_messages = {
        'incorrect_type': 'Incorrect type. Expected a list, but got {input}',
        'type_error': '类型不正确',
        'not_null': '类型必填'
    }

    def to_internal_value(self, data):
        category = ['上游', '下游']
        if not isinstance(data, list):
            self.fail('incorrect_type', input=type(data).__name__)
        if not data:
            self.fail('not_null')
        for e in data:
            if e not in category:
                self.fail('type_error')
        return data

class SnippetCreateSerializer(serializers.Serializer):
    list = Customfield()





