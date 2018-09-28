from django.db import models
import ast

class ListField(models.TextField):
     description = "Stores a python list"

     def __init__(self, *args, **kwargs):
         super(ListField, self).__init__(*args, **kwargs)

     def to_python(self, value):
         if not value:
             value = []

         if isinstance(value, list):
             return value

         return ast.literal_eval(value)

     def get_prep_value(self, value):
         if value is None:
             return value

         return str(value)

     def value_to_string(self, obj):
         super(ListField, self).value_to_string(obj)