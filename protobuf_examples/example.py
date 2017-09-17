from protobuf_decoder import ProtobufDecoder

import basic_pb2 as basic

proto_decoder = ProtobufDecoder(protobuf_modules=[basic])


# Create a basic protobuf object
person = basic.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = basic.Person.HOME

# Serialize protobuf
serialized = person.SerializeToString()

# Dummy send :-)
pass

# Deserialize protobuf 
obj = proto_decoder.deserialize_string(serialized)
print(obj)
