# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forbes.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x66orbes.proto\x12\nforbesdata\"O\n\x0b\x42illionaire\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x14\n\x0corganization\x18\x04 \x01(\t\"\x18\n\x16GetBillionairesRequest\"H\n\x17GetBillionairesResponse\x12-\n\x0c\x62illionaires\x18\x01 \x03(\x0b\x32\x17.forbesdata.Billionaire\".\n\x1eGetBillionaireBioByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x1fGetBillionaireBioByNameResponse\x12,\n\x0b\x62illionaire\x18\x01 \x03(\x0b\x32\x17.forbesdata.Billionaire2\xdc\x01\n\x06\x46orbes\x12\\\n\x0fGetBillionaires\x12\".forbesdata.GetBillionairesRequest\x1a#.forbesdata.GetBillionairesResponse\"\x00\x12t\n\x17GetBillionaireBioByName\x12*.forbesdata.GetBillionaireBioByNameRequest\x1a+.forbesdata.GetBillionaireBioByNameResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'forbes_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BILLIONAIRE._serialized_start=28
  _BILLIONAIRE._serialized_end=107
  _GETBILLIONAIRESREQUEST._serialized_start=109
  _GETBILLIONAIRESREQUEST._serialized_end=133
  _GETBILLIONAIRESRESPONSE._serialized_start=135
  _GETBILLIONAIRESRESPONSE._serialized_end=207
  _GETBILLIONAIREBIOBYNAMEREQUEST._serialized_start=209
  _GETBILLIONAIREBIOBYNAMEREQUEST._serialized_end=255
  _GETBILLIONAIREBIOBYNAMERESPONSE._serialized_start=257
  _GETBILLIONAIREBIOBYNAMERESPONSE._serialized_end=336
  _FORBES._serialized_start=339
  _FORBES._serialized_end=559
# @@protoc_insertion_point(module_scope)
