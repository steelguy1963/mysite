from django.core.serializers.json import Serializer

class Serializer(Serializer):
    def get_dump_object(self, obj):
        return self.__current
    def start_serialization(self):
        super(Serializer, self).start_serialization()
        self.json_kwargs["ensure_ascii"]=False
        self.json_kwargs['indent']=2