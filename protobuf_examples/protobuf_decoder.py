import inspect
from google.protobuf.message import DecodeError

# Takes imported protobuf modules and tries to decode objects from strings
class ProtobufDecoder:

    def __init__(self, protobuf_modules):
        self.protobuf_classes = self.get_protobuf_classes(protobuf_modules)
    
    # Tries to decode serialized message from known protobuf classes
    def deserialize_string(self, serialized_obj):

        for cls in self.protobuf_classes:
            try:
                cls_instance = cls()
                cls_instance.ParseFromString(serialized_obj)
                return cls_instance
            except DecodeError:
                pass

    # Saves classes from protobuf_modules.
    # WARNING!: Has only been tested with actual protobuf modules, don't import anything else :-)
    def get_protobuf_classes(self, protobuf_modules):
        protobuf_classes = []

        for protobuf_file in protobuf_modules:
            for name, obj in inspect.getmembers(protobuf_file):
                if inspect.isclass(obj):
                    print(obj)
                    protobuf_classes.append(obj)

        return protobuf_classes