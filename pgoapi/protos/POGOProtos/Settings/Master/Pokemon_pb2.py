# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Settings.Master.Pokemon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos import Enums_pb2 as POGOProtos_dot_Enums__pb2

from POGOProtos.Enums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Settings.Master.Pokemon.proto',
  package='POGOProtos.Settings.Master.Pokemon',
  syntax='proto3',
  serialized_pb=_b('\n(POGOProtos.Settings.Master.Pokemon.proto\x12\"POGOProtos.Settings.Master.Pokemon\x1a\x16POGOProtos.Enums.proto\"\xa6\x02\n\x13\x45ncounterAttributes\x12\x19\n\x11\x62\x61se_capture_rate\x18\x01 \x01(\x02\x12\x16\n\x0e\x62\x61se_flee_rate\x18\x02 \x01(\x02\x12\x1a\n\x12\x63ollision_radius_m\x18\x03 \x01(\x02\x12\x1a\n\x12\x63ollision_height_m\x18\x04 \x01(\x02\x12\x1f\n\x17\x63ollision_head_radius_m\x18\x05 \x01(\x02\x12<\n\rmovement_type\x18\x06 \x01(\x0e\x32%.POGOProtos.Enums.PokemonMovementType\x12\x18\n\x10movement_timer_s\x18\x07 \x01(\x02\x12\x13\n\x0bjump_time_s\x18\x08 \x01(\x02\x12\x16\n\x0e\x61ttack_timer_s\x18\t \x01(\x02\"\x97\x01\n\x10\x43\x61meraAttributes\x12\x15\n\rdisk_radius_m\x18\x01 \x01(\x02\x12\x19\n\x11\x63ylinder_radius_m\x18\x02 \x01(\x02\x12\x19\n\x11\x63ylinder_height_m\x18\x03 \x01(\x02\x12\x19\n\x11\x63ylinder_ground_m\x18\x04 \x01(\x02\x12\x1b\n\x13shoulder_mode_scale\x18\x05 \x01(\x02\"n\n\x0fStatsAttributes\x12\x14\n\x0c\x62\x61se_stamina\x18\x01 \x01(\x05\x12\x13\n\x0b\x62\x61se_attack\x18\x02 \x01(\x05\x12\x14\n\x0c\x62\x61se_defense\x18\x03 \x01(\x05\x12\x1a\n\x12\x64odge_energy_delta\x18\x08 \x01(\x05P\x00\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENCOUNTERATTRIBUTES = _descriptor.Descriptor(
  name='EncounterAttributes',
  full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_capture_rate', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.base_capture_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_flee_rate', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.base_flee_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_radius_m', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.collision_radius_m', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_height_m', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.collision_height_m', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_head_radius_m', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.collision_head_radius_m', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='movement_type', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.movement_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='movement_timer_s', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.movement_timer_s', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jump_time_s', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.jump_time_s', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack_timer_s', full_name='POGOProtos.Settings.Master.Pokemon.EncounterAttributes.attack_timer_s', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=399,
)


_CAMERAATTRIBUTES = _descriptor.Descriptor(
  name='CameraAttributes',
  full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_radius_m', full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes.disk_radius_m', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cylinder_radius_m', full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes.cylinder_radius_m', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cylinder_height_m', full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes.cylinder_height_m', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cylinder_ground_m', full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes.cylinder_ground_m', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shoulder_mode_scale', full_name='POGOProtos.Settings.Master.Pokemon.CameraAttributes.shoulder_mode_scale', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=553,
)


_STATSATTRIBUTES = _descriptor.Descriptor(
  name='StatsAttributes',
  full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_stamina', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_stamina', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_attack', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_attack', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_defense', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_defense', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodge_energy_delta', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.dodge_energy_delta', index=3,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=665,
)

_ENCOUNTERATTRIBUTES.fields_by_name['movement_type'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONMOVEMENTTYPE
DESCRIPTOR.message_types_by_name['EncounterAttributes'] = _ENCOUNTERATTRIBUTES
DESCRIPTOR.message_types_by_name['CameraAttributes'] = _CAMERAATTRIBUTES
DESCRIPTOR.message_types_by_name['StatsAttributes'] = _STATSATTRIBUTES

EncounterAttributes = _reflection.GeneratedProtocolMessageType('EncounterAttributes', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERATTRIBUTES,
  __module__ = 'POGOProtos.Settings.Master.Pokemon_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.Pokemon.EncounterAttributes)
  ))
_sym_db.RegisterMessage(EncounterAttributes)

CameraAttributes = _reflection.GeneratedProtocolMessageType('CameraAttributes', (_message.Message,), dict(
  DESCRIPTOR = _CAMERAATTRIBUTES,
  __module__ = 'POGOProtos.Settings.Master.Pokemon_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.Pokemon.CameraAttributes)
  ))
_sym_db.RegisterMessage(CameraAttributes)

StatsAttributes = _reflection.GeneratedProtocolMessageType('StatsAttributes', (_message.Message,), dict(
  DESCRIPTOR = _STATSATTRIBUTES,
  __module__ = 'POGOProtos.Settings.Master.Pokemon_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.Pokemon.StatsAttributes)
  ))
_sym_db.RegisterMessage(StatsAttributes)


# @@protoc_insertion_point(module_scope)
