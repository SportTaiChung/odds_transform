# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: APHDC.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='APHDC.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=_b('\n\"jst.java.mservice.catcher.protobufB\005APHDC'),
  serialized_pb=_b('\n\x0b\x41PHDC.proto\x12\x08protobuf\"*\n\x08\x41pHdcArr\x12\x1e\n\x05\x61phdc\x18\x01 \x03(\x0b\x32\x0f.protobuf.ApHdc\"\x80\x05\n\x05\x41pHdc\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x12\n\ngame_class\x18\x02 \x01(\t\x12\x11\n\tgame_type\x18\x03 \x01(\t\x12\x14\n\x0craw_event_id\x18\x04 \x01(\t\x12\x0f\n\x07game_id\x18\x05 \x01(\t\x12\n\n\x02ip\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x12\n\nevent_time\x18\x08 \x01(\t\x12\x19\n\x11source_updatetime\x18\t \x01(\t\x12\x0c\n\x04live\x18\n \x01(\t\x12\x11\n\tlive_time\x18\x0b \x01(\t\x12*\n\x0binformation\x18\x0c \x01(\x0b\x32\x15.protobuf.information\x12\x1e\n\x05score\x18\r \x01(\x0b\x32\x0f.protobuf.score\x12\"\n\x07redcard\x18\x0e \x01(\x0b\x32\x11.protobuf.redcard\x12(\n\nyellowcard\x18\x0f \x01(\x0b\x32\x14.protobuf.yellowcard\x12 \n\x06\x63onner\x18\x10 \x01(\x0b\x32\x10.protobuf.conner\x12\x1c\n\x04usZF\x18\x11 \x01(\x0b\x32\x0e.protobuf.usZF\x12\x1e\n\x04usDS\x18\x12 \x01(\x0b\x32\x10.protobuf.typeDS\x12\x1c\n\x04twZF\x18\x13 \x01(\x0b\x32\x0e.protobuf.twZF\x12\x1e\n\x04twDS\x18\x14 \x01(\x0b\x32\x10.protobuf.typeDS\x12\x1c\n\x02\x64\x65\x18\x15 \x01(\x0b\x32\x10.protobuf.onetwo\x12\x1c\n\x02sd\x18\x16 \x01(\x0b\x32\x10.protobuf.onetwo\x12\x1c\n\x04\x65sre\x18\x17 \x01(\x0b\x32\x0e.protobuf.Esre\x12\x0c\n\x04\x64raw\x18\x18 \x01(\t\x12\r\n\x05multi\x18\x19 \x01(\t\"D\n\x04\x45sre\x12 \n\x03let\x18\x01 \x01(\x0e\x32\x13.protobuf.whichTeam\x12\x0c\n\x04home\x18\x02 \x01(\t\x12\x0c\n\x04\x61way\x18\x03 \x01(\t\"$\n\x06onetwo\x12\x0c\n\x04home\x18\x01 \x01(\t\x12\x0c\n\x04\x61way\x18\x02 \x01(\t\"J\n\x04usZF\x12 \n\x06homeZF\x18\x01 \x01(\x0b\x32\x10.protobuf.typeZF\x12 \n\x06\x61wayZF\x18\x02 \x01(\x0b\x32\x10.protobuf.typeZF\"J\n\x04twZF\x12 \n\x06homeZF\x18\x01 \x01(\x0b\x32\x10.protobuf.typeZF\x12 \n\x06\x61wayZF\x18\x02 \x01(\x0b\x32\x10.protobuf.typeZF\"3\n\x06typeDS\x12\x0c\n\x04line\x18\x01 \x01(\t\x12\x0c\n\x04over\x18\x02 \x01(\t\x12\r\n\x05under\x18\x03 \x01(\t\"$\n\x06typeZF\x12\x0c\n\x04line\x18\x01 \x01(\t\x12\x0c\n\x04odds\x18\x02 \x01(\t\"#\n\x05score\x12\x0c\n\x04home\x18\x01 \x01(\t\x12\x0c\n\x04\x61way\x18\x02 \x01(\t\"%\n\x07redcard\x12\x0c\n\x04home\x18\x01 \x01(\t\x12\x0c\n\x04\x61way\x18\x02 \x01(\t\"(\n\nyellowcard\x12\x0c\n\x04home\x18\x01 \x01(\t\x12\x0c\n\x04\x61way\x18\x02 \x01(\t\"$\n\x06\x63onner\x12\x0c\n\x04home\x18\x01 \x01(\t\x12\x0c\n\x04\x61way\x18\x02 \x01(\t\"\x83\x01\n\x0binformation\x12\x0e\n\x06league\x18\x01 \x01(\t\x12\x11\n\tcn_league\x18\x02 \x01(\t\x12\x11\n\ten_league\x18\x03 \x01(\t\x12\x1e\n\x04home\x18\x04 \x01(\x0b\x32\x10.protobuf.infoHA\x12\x1e\n\x04\x61way\x18\x05 \x01(\x0b\x32\x10.protobuf.infoHA\"N\n\x06infoHA\x12\x11\n\tteam_name\x18\x01 \x01(\t\x12\x0f\n\x07pitcher\x18\x02 \x01(\t\x12\x0f\n\x07\x63n_name\x18\x03 \x01(\t\x12\x0f\n\x07\x65n_name\x18\x04 \x01(\t*)\n\twhichTeam\x12\x08\n\x04none\x10\x00\x12\x08\n\x04home\x10\x01\x12\x08\n\x04\x61way\x10\x02\x42+\n\"jst.java.mservice.catcher.protobufB\x05\x41PHDCb\x06proto3')
)

_WHICHTEAM = _descriptor.EnumDescriptor(
  name='whichTeam',
  full_name='protobuf.whichTeam',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='none', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='home', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='away', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1433,
  serialized_end=1474,
)
_sym_db.RegisterEnumDescriptor(_WHICHTEAM)

whichTeam = enum_type_wrapper.EnumTypeWrapper(_WHICHTEAM)
none = 0
home = 1
away = 2



_APHDCARR = _descriptor.Descriptor(
  name='ApHdcArr',
  full_name='protobuf.ApHdcArr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aphdc', full_name='protobuf.ApHdcArr.aphdc', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=67,
)


_APHDC = _descriptor.Descriptor(
  name='ApHdc',
  full_name='protobuf.ApHdc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='protobuf.ApHdc.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_class', full_name='protobuf.ApHdc.game_class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_type', full_name='protobuf.ApHdc.game_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_event_id', full_name='protobuf.ApHdc.raw_event_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='protobuf.ApHdc.game_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='protobuf.ApHdc.ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='protobuf.ApHdc.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='protobuf.ApHdc.event_time', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_updatetime', full_name='protobuf.ApHdc.source_updatetime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live', full_name='protobuf.ApHdc.live', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live_time', full_name='protobuf.ApHdc.live_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='information', full_name='protobuf.ApHdc.information', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='protobuf.ApHdc.score', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redcard', full_name='protobuf.ApHdc.redcard', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yellowcard', full_name='protobuf.ApHdc.yellowcard', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conner', full_name='protobuf.ApHdc.conner', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usZF', full_name='protobuf.ApHdc.usZF', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usDS', full_name='protobuf.ApHdc.usDS', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twZF', full_name='protobuf.ApHdc.twZF', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twDS', full_name='protobuf.ApHdc.twDS', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='de', full_name='protobuf.ApHdc.de', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sd', full_name='protobuf.ApHdc.sd', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='esre', full_name='protobuf.ApHdc.esre', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw', full_name='protobuf.ApHdc.draw', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi', full_name='protobuf.ApHdc.multi', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=710,
)


_ESRE = _descriptor.Descriptor(
  name='Esre',
  full_name='protobuf.Esre',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='let', full_name='protobuf.Esre.let', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.Esre.home', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.Esre.away', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=780,
)


_ONETWO = _descriptor.Descriptor(
  name='onetwo',
  full_name='protobuf.onetwo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.onetwo.home', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.onetwo.away', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=782,
  serialized_end=818,
)


_USZF = _descriptor.Descriptor(
  name='usZF',
  full_name='protobuf.usZF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='homeZF', full_name='protobuf.usZF.homeZF', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='awayZF', full_name='protobuf.usZF.awayZF', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=820,
  serialized_end=894,
)


_TWZF = _descriptor.Descriptor(
  name='twZF',
  full_name='protobuf.twZF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='homeZF', full_name='protobuf.twZF.homeZF', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='awayZF', full_name='protobuf.twZF.awayZF', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=896,
  serialized_end=970,
)


_TYPEDS = _descriptor.Descriptor(
  name='typeDS',
  full_name='protobuf.typeDS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='protobuf.typeDS.line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='over', full_name='protobuf.typeDS.over', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='under', full_name='protobuf.typeDS.under', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1023,
)


_TYPEZF = _descriptor.Descriptor(
  name='typeZF',
  full_name='protobuf.typeZF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='protobuf.typeZF.line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='odds', full_name='protobuf.typeZF.odds', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1061,
)


_SCORE = _descriptor.Descriptor(
  name='score',
  full_name='protobuf.score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.score.home', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.score.away', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1063,
  serialized_end=1098,
)


_REDCARD = _descriptor.Descriptor(
  name='redcard',
  full_name='protobuf.redcard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.redcard.home', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.redcard.away', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1100,
  serialized_end=1137,
)


_YELLOWCARD = _descriptor.Descriptor(
  name='yellowcard',
  full_name='protobuf.yellowcard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.yellowcard.home', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.yellowcard.away', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1139,
  serialized_end=1179,
)


_CONNER = _descriptor.Descriptor(
  name='conner',
  full_name='protobuf.conner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.conner.home', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.conner.away', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1181,
  serialized_end=1217,
)


_INFORMATION = _descriptor.Descriptor(
  name='information',
  full_name='protobuf.information',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='league', full_name='protobuf.information.league', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cn_league', full_name='protobuf.information.cn_league', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='en_league', full_name='protobuf.information.en_league', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home', full_name='protobuf.information.home', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='protobuf.information.away', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1220,
  serialized_end=1351,
)


_INFOHA = _descriptor.Descriptor(
  name='infoHA',
  full_name='protobuf.infoHA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_name', full_name='protobuf.infoHA.team_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitcher', full_name='protobuf.infoHA.pitcher', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cn_name', full_name='protobuf.infoHA.cn_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='en_name', full_name='protobuf.infoHA.en_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1353,
  serialized_end=1431,
)

_APHDCARR.fields_by_name['aphdc'].message_type = _APHDC
_APHDC.fields_by_name['information'].message_type = _INFORMATION
_APHDC.fields_by_name['score'].message_type = _SCORE
_APHDC.fields_by_name['redcard'].message_type = _REDCARD
_APHDC.fields_by_name['yellowcard'].message_type = _YELLOWCARD
_APHDC.fields_by_name['conner'].message_type = _CONNER
_APHDC.fields_by_name['usZF'].message_type = _USZF
_APHDC.fields_by_name['usDS'].message_type = _TYPEDS
_APHDC.fields_by_name['twZF'].message_type = _TWZF
_APHDC.fields_by_name['twDS'].message_type = _TYPEDS
_APHDC.fields_by_name['de'].message_type = _ONETWO
_APHDC.fields_by_name['sd'].message_type = _ONETWO
_APHDC.fields_by_name['esre'].message_type = _ESRE
_ESRE.fields_by_name['let'].enum_type = _WHICHTEAM
_USZF.fields_by_name['homeZF'].message_type = _TYPEZF
_USZF.fields_by_name['awayZF'].message_type = _TYPEZF
_TWZF.fields_by_name['homeZF'].message_type = _TYPEZF
_TWZF.fields_by_name['awayZF'].message_type = _TYPEZF
_INFORMATION.fields_by_name['home'].message_type = _INFOHA
_INFORMATION.fields_by_name['away'].message_type = _INFOHA
DESCRIPTOR.message_types_by_name['ApHdcArr'] = _APHDCARR
DESCRIPTOR.message_types_by_name['ApHdc'] = _APHDC
DESCRIPTOR.message_types_by_name['Esre'] = _ESRE
DESCRIPTOR.message_types_by_name['onetwo'] = _ONETWO
DESCRIPTOR.message_types_by_name['usZF'] = _USZF
DESCRIPTOR.message_types_by_name['twZF'] = _TWZF
DESCRIPTOR.message_types_by_name['typeDS'] = _TYPEDS
DESCRIPTOR.message_types_by_name['typeZF'] = _TYPEZF
DESCRIPTOR.message_types_by_name['score'] = _SCORE
DESCRIPTOR.message_types_by_name['redcard'] = _REDCARD
DESCRIPTOR.message_types_by_name['yellowcard'] = _YELLOWCARD
DESCRIPTOR.message_types_by_name['conner'] = _CONNER
DESCRIPTOR.message_types_by_name['information'] = _INFORMATION
DESCRIPTOR.message_types_by_name['infoHA'] = _INFOHA
DESCRIPTOR.enum_types_by_name['whichTeam'] = _WHICHTEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApHdcArr = _reflection.GeneratedProtocolMessageType('ApHdcArr', (_message.Message,), dict(
  DESCRIPTOR = _APHDCARR,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.ApHdcArr)
  ))
_sym_db.RegisterMessage(ApHdcArr)

ApHdc = _reflection.GeneratedProtocolMessageType('ApHdc', (_message.Message,), dict(
  DESCRIPTOR = _APHDC,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.ApHdc)
  ))
_sym_db.RegisterMessage(ApHdc)

Esre = _reflection.GeneratedProtocolMessageType('Esre', (_message.Message,), dict(
  DESCRIPTOR = _ESRE,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Esre)
  ))
_sym_db.RegisterMessage(Esre)

onetwo = _reflection.GeneratedProtocolMessageType('onetwo', (_message.Message,), dict(
  DESCRIPTOR = _ONETWO,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.onetwo)
  ))
_sym_db.RegisterMessage(onetwo)

usZF = _reflection.GeneratedProtocolMessageType('usZF', (_message.Message,), dict(
  DESCRIPTOR = _USZF,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.usZF)
  ))
_sym_db.RegisterMessage(usZF)

twZF = _reflection.GeneratedProtocolMessageType('twZF', (_message.Message,), dict(
  DESCRIPTOR = _TWZF,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.twZF)
  ))
_sym_db.RegisterMessage(twZF)

typeDS = _reflection.GeneratedProtocolMessageType('typeDS', (_message.Message,), dict(
  DESCRIPTOR = _TYPEDS,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.typeDS)
  ))
_sym_db.RegisterMessage(typeDS)

typeZF = _reflection.GeneratedProtocolMessageType('typeZF', (_message.Message,), dict(
  DESCRIPTOR = _TYPEZF,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.typeZF)
  ))
_sym_db.RegisterMessage(typeZF)

score = _reflection.GeneratedProtocolMessageType('score', (_message.Message,), dict(
  DESCRIPTOR = _SCORE,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.score)
  ))
_sym_db.RegisterMessage(score)

redcard = _reflection.GeneratedProtocolMessageType('redcard', (_message.Message,), dict(
  DESCRIPTOR = _REDCARD,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.redcard)
  ))
_sym_db.RegisterMessage(redcard)

yellowcard = _reflection.GeneratedProtocolMessageType('yellowcard', (_message.Message,), dict(
  DESCRIPTOR = _YELLOWCARD,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.yellowcard)
  ))
_sym_db.RegisterMessage(yellowcard)

conner = _reflection.GeneratedProtocolMessageType('conner', (_message.Message,), dict(
  DESCRIPTOR = _CONNER,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.conner)
  ))
_sym_db.RegisterMessage(conner)

information = _reflection.GeneratedProtocolMessageType('information', (_message.Message,), dict(
  DESCRIPTOR = _INFORMATION,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.information)
  ))
_sym_db.RegisterMessage(information)

infoHA = _reflection.GeneratedProtocolMessageType('infoHA', (_message.Message,), dict(
  DESCRIPTOR = _INFOHA,
  __module__ = 'APHDC_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.infoHA)
  ))
_sym_db.RegisterMessage(infoHA)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
