# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: elb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='elb.proto',
  package='elb',
  serialized_pb=_b('\n\telb.proto\x12\x03\x65lb\"$\n\x08HostAddr\x12\n\n\x02ip\x18\x01 \x02(\x05\x12\x0c\n\x04port\x18\x02 \x02(\x05\"7\n\nGetHostReq\x12\x0b\n\x03seq\x18\x01 \x02(\r\x12\r\n\x05modid\x18\x02 \x02(\x05\x12\r\n\x05\x63mdid\x18\x03 \x02(\x05\"e\n\nGetHostRsp\x12\x0b\n\x03seq\x18\x01 \x02(\r\x12\r\n\x05modid\x18\x02 \x02(\x05\x12\r\n\x05\x63mdid\x18\x03 \x02(\x05\x12\x0f\n\x07retcode\x18\x04 \x02(\x05\x12\x1b\n\x04host\x18\x05 \x01(\x0b\x32\r.elb.HostAddr\"W\n\tReportReq\x12\r\n\x05modid\x18\x01 \x02(\x05\x12\r\n\x05\x63mdid\x18\x02 \x02(\x05\x12\x1b\n\x04host\x18\x03 \x02(\x0b\x32\r.elb.HostAddr\x12\x0f\n\x07retcode\x18\x04 \x02(\x05\"+\n\x0bGetRouteReq\x12\r\n\x05modid\x18\x01 \x02(\x05\x12\r\n\x05\x63mdid\x18\x02 \x02(\x05\"I\n\x0bGetRouteRsp\x12\r\n\x05modid\x18\x01 \x02(\x05\x12\r\n\x05\x63mdid\x18\x02 \x02(\x05\x12\x1c\n\x05hosts\x18\x03 \x03(\x0b\x32\r.elb.HostAddr\"E\n\x0eHostCallResult\x12\n\n\x02ip\x18\x01 \x02(\x05\x12\x0c\n\x04port\x18\x02 \x02(\x05\x12\x0c\n\x04succ\x18\x03 \x02(\r\x12\x0b\n\x03\x65rr\x18\x04 \x02(\r\"\x83\x01\n\x0fReportStatusReq\x12\r\n\x05modid\x18\x01 \x02(\x05\x12\r\n\x05\x63mdid\x18\x02 \x02(\x05\x12\x0e\n\x06\x63\x61ller\x18\x03 \x02(\x05\x12$\n\x07results\x18\x04 \x03(\x0b\x32\x13.elb.HostCallResult\x12\n\n\x02ts\x18\x05 \x02(\r\x12\x10\n\x08overload\x18\x06 \x02(\x08*\xbd\x01\n\tMsgTypeId\x12\x10\n\x0cGetHostReqId\x10\x01\x12\x10\n\x0cGetHostRspId\x10\x02\x12\x0f\n\x0bReportReqId\x10\x03\x12\x17\n\x13GetRouteByToolReqId\x10\x04\x12\x17\n\x13GetRouteByToolRspId\x10\x05\x12\x18\n\x14GetRouteByAgentReqId\x10\x06\x12\x18\n\x14GetRouteByAgentRspId\x10\x07\x12\x15\n\x11ReportStatusReqId\x10\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGTYPEID = _descriptor.EnumDescriptor(
  name='MsgTypeId',
  full_name='elb.MsgTypeId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GetHostReqId', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GetHostRspId', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReportReqId', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GetRouteByToolReqId', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GetRouteByToolRspId', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GetRouteByAgentReqId', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GetRouteByAgentRspId', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReportStatusReqId', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=631,
  serialized_end=820,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPEID)

MsgTypeId = enum_type_wrapper.EnumTypeWrapper(_MSGTYPEID)
GetHostReqId = 1
GetHostRspId = 2
ReportReqId = 3
GetRouteByToolReqId = 4
GetRouteByToolRspId = 5
GetRouteByAgentReqId = 6
GetRouteByAgentRspId = 7
ReportStatusReqId = 8



_HOSTADDR = _descriptor.Descriptor(
  name='HostAddr',
  full_name='elb.HostAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='elb.HostAddr.ip', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='elb.HostAddr.port', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=54,
)


_GETHOSTREQ = _descriptor.Descriptor(
  name='GetHostReq',
  full_name='elb.GetHostReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='elb.GetHostReq.seq', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.GetHostReq.modid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.GetHostReq.cmdid', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=111,
)


_GETHOSTRSP = _descriptor.Descriptor(
  name='GetHostRsp',
  full_name='elb.GetHostRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='elb.GetHostRsp.seq', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.GetHostRsp.modid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.GetHostRsp.cmdid', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retcode', full_name='elb.GetHostRsp.retcode', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='elb.GetHostRsp.host', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=214,
)


_REPORTREQ = _descriptor.Descriptor(
  name='ReportReq',
  full_name='elb.ReportReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.ReportReq.modid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.ReportReq.cmdid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='elb.ReportReq.host', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retcode', full_name='elb.ReportReq.retcode', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=303,
)


_GETROUTEREQ = _descriptor.Descriptor(
  name='GetRouteReq',
  full_name='elb.GetRouteReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.GetRouteReq.modid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.GetRouteReq.cmdid', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=348,
)


_GETROUTERSP = _descriptor.Descriptor(
  name='GetRouteRsp',
  full_name='elb.GetRouteRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.GetRouteRsp.modid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.GetRouteRsp.cmdid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='elb.GetRouteRsp.hosts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=423,
)


_HOSTCALLRESULT = _descriptor.Descriptor(
  name='HostCallResult',
  full_name='elb.HostCallResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='elb.HostCallResult.ip', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='elb.HostCallResult.port', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='succ', full_name='elb.HostCallResult.succ', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='elb.HostCallResult.err', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=494,
)


_REPORTSTATUSREQ = _descriptor.Descriptor(
  name='ReportStatusReq',
  full_name='elb.ReportStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modid', full_name='elb.ReportStatusReq.modid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='elb.ReportStatusReq.cmdid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller', full_name='elb.ReportStatusReq.caller', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='elb.ReportStatusReq.results', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts', full_name='elb.ReportStatusReq.ts', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overload', full_name='elb.ReportStatusReq.overload', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=628,
)

_GETHOSTRSP.fields_by_name['host'].message_type = _HOSTADDR
_REPORTREQ.fields_by_name['host'].message_type = _HOSTADDR
_GETROUTERSP.fields_by_name['hosts'].message_type = _HOSTADDR
_REPORTSTATUSREQ.fields_by_name['results'].message_type = _HOSTCALLRESULT
DESCRIPTOR.message_types_by_name['HostAddr'] = _HOSTADDR
DESCRIPTOR.message_types_by_name['GetHostReq'] = _GETHOSTREQ
DESCRIPTOR.message_types_by_name['GetHostRsp'] = _GETHOSTRSP
DESCRIPTOR.message_types_by_name['ReportReq'] = _REPORTREQ
DESCRIPTOR.message_types_by_name['GetRouteReq'] = _GETROUTEREQ
DESCRIPTOR.message_types_by_name['GetRouteRsp'] = _GETROUTERSP
DESCRIPTOR.message_types_by_name['HostCallResult'] = _HOSTCALLRESULT
DESCRIPTOR.message_types_by_name['ReportStatusReq'] = _REPORTSTATUSREQ
DESCRIPTOR.enum_types_by_name['MsgTypeId'] = _MSGTYPEID

HostAddr = _reflection.GeneratedProtocolMessageType('HostAddr', (_message.Message,), dict(
  DESCRIPTOR = _HOSTADDR,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.HostAddr)
  ))
_sym_db.RegisterMessage(HostAddr)

GetHostReq = _reflection.GeneratedProtocolMessageType('GetHostReq', (_message.Message,), dict(
  DESCRIPTOR = _GETHOSTREQ,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.GetHostReq)
  ))
_sym_db.RegisterMessage(GetHostReq)

GetHostRsp = _reflection.GeneratedProtocolMessageType('GetHostRsp', (_message.Message,), dict(
  DESCRIPTOR = _GETHOSTRSP,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.GetHostRsp)
  ))
_sym_db.RegisterMessage(GetHostRsp)

ReportReq = _reflection.GeneratedProtocolMessageType('ReportReq', (_message.Message,), dict(
  DESCRIPTOR = _REPORTREQ,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.ReportReq)
  ))
_sym_db.RegisterMessage(ReportReq)

GetRouteReq = _reflection.GeneratedProtocolMessageType('GetRouteReq', (_message.Message,), dict(
  DESCRIPTOR = _GETROUTEREQ,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.GetRouteReq)
  ))
_sym_db.RegisterMessage(GetRouteReq)

GetRouteRsp = _reflection.GeneratedProtocolMessageType('GetRouteRsp', (_message.Message,), dict(
  DESCRIPTOR = _GETROUTERSP,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.GetRouteRsp)
  ))
_sym_db.RegisterMessage(GetRouteRsp)

HostCallResult = _reflection.GeneratedProtocolMessageType('HostCallResult', (_message.Message,), dict(
  DESCRIPTOR = _HOSTCALLRESULT,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.HostCallResult)
  ))
_sym_db.RegisterMessage(HostCallResult)

ReportStatusReq = _reflection.GeneratedProtocolMessageType('ReportStatusReq', (_message.Message,), dict(
  DESCRIPTOR = _REPORTSTATUSREQ,
  __module__ = 'elb_pb2'
  # @@protoc_insertion_point(class_scope:elb.ReportStatusReq)
  ))
_sym_db.RegisterMessage(ReportStatusReq)


# @@protoc_insertion_point(module_scope)
