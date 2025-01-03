// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: basic.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_basic_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_basic_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3012000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3012004 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_basic_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_basic_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[4]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_basic_2eproto;
namespace et {
namespace proto {
class Bool;
class BoolDefaultTypeInternal;
extern BoolDefaultTypeInternal _Bool_default_instance_;
class Double;
class DoubleDefaultTypeInternal;
extern DoubleDefaultTypeInternal _Double_default_instance_;
class Int;
class IntDefaultTypeInternal;
extern IntDefaultTypeInternal _Int_default_instance_;
class Str;
class StrDefaultTypeInternal;
extern StrDefaultTypeInternal _Str_default_instance_;
}  // namespace proto
}  // namespace et
PROTOBUF_NAMESPACE_OPEN
template<> ::et::proto::Bool* Arena::CreateMaybeMessage<::et::proto::Bool>(Arena*);
template<> ::et::proto::Double* Arena::CreateMaybeMessage<::et::proto::Double>(Arena*);
template<> ::et::proto::Int* Arena::CreateMaybeMessage<::et::proto::Int>(Arena*);
template<> ::et::proto::Str* Arena::CreateMaybeMessage<::et::proto::Str>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace et {
namespace proto {

// ===================================================================

class Bool PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:et.proto.Bool) */ {
 public:
  inline Bool() : Bool(nullptr) {};
  virtual ~Bool();

  Bool(const Bool& from);
  Bool(Bool&& from) noexcept
    : Bool() {
    *this = ::std::move(from);
  }

  inline Bool& operator=(const Bool& from) {
    CopyFrom(from);
    return *this;
  }
  inline Bool& operator=(Bool&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const Bool& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Bool* internal_default_instance() {
    return reinterpret_cast<const Bool*>(
               &_Bool_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(Bool& a, Bool& b) {
    a.Swap(&b);
  }
  inline void Swap(Bool* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Bool* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Bool* New() const final {
    return CreateMaybeMessage<Bool>(nullptr);
  }

  Bool* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Bool>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const Bool& from);
  void MergeFrom(const Bool& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Bool* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "et.proto.Bool";
  }
  protected:
  explicit Bool(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_basic_2eproto);
    return ::descriptor_table_basic_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kValFieldNumber = 1,
  };
  // bool val = 1;
  void clear_val();
  bool val() const;
  void set_val(bool value);
  private:
  bool _internal_val() const;
  void _internal_set_val(bool value);
  public:

  // @@protoc_insertion_point(class_scope:et.proto.Bool)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  bool val_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_basic_2eproto;
};
// -------------------------------------------------------------------

class Int PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:et.proto.Int) */ {
 public:
  inline Int() : Int(nullptr) {};
  virtual ~Int();

  Int(const Int& from);
  Int(Int&& from) noexcept
    : Int() {
    *this = ::std::move(from);
  }

  inline Int& operator=(const Int& from) {
    CopyFrom(from);
    return *this;
  }
  inline Int& operator=(Int&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const Int& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Int* internal_default_instance() {
    return reinterpret_cast<const Int*>(
               &_Int_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(Int& a, Int& b) {
    a.Swap(&b);
  }
  inline void Swap(Int* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Int* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Int* New() const final {
    return CreateMaybeMessage<Int>(nullptr);
  }

  Int* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Int>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const Int& from);
  void MergeFrom(const Int& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Int* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "et.proto.Int";
  }
  protected:
  explicit Int(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_basic_2eproto);
    return ::descriptor_table_basic_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kValFieldNumber = 1,
  };
  // int32 val = 1;
  void clear_val();
  ::PROTOBUF_NAMESPACE_ID::int32 val() const;
  void set_val(::PROTOBUF_NAMESPACE_ID::int32 value);
  private:
  ::PROTOBUF_NAMESPACE_ID::int32 _internal_val() const;
  void _internal_set_val(::PROTOBUF_NAMESPACE_ID::int32 value);
  public:

  // @@protoc_insertion_point(class_scope:et.proto.Int)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::int32 val_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_basic_2eproto;
};
// -------------------------------------------------------------------

class Double PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:et.proto.Double) */ {
 public:
  inline Double() : Double(nullptr) {};
  virtual ~Double();

  Double(const Double& from);
  Double(Double&& from) noexcept
    : Double() {
    *this = ::std::move(from);
  }

  inline Double& operator=(const Double& from) {
    CopyFrom(from);
    return *this;
  }
  inline Double& operator=(Double&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const Double& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Double* internal_default_instance() {
    return reinterpret_cast<const Double*>(
               &_Double_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    2;

  friend void swap(Double& a, Double& b) {
    a.Swap(&b);
  }
  inline void Swap(Double* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Double* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Double* New() const final {
    return CreateMaybeMessage<Double>(nullptr);
  }

  Double* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Double>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const Double& from);
  void MergeFrom(const Double& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Double* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "et.proto.Double";
  }
  protected:
  explicit Double(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_basic_2eproto);
    return ::descriptor_table_basic_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kValFieldNumber = 1,
  };
  // double val = 1;
  void clear_val();
  double val() const;
  void set_val(double value);
  private:
  double _internal_val() const;
  void _internal_set_val(double value);
  public:

  // @@protoc_insertion_point(class_scope:et.proto.Double)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  double val_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_basic_2eproto;
};
// -------------------------------------------------------------------

class Str PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:et.proto.Str) */ {
 public:
  inline Str() : Str(nullptr) {};
  virtual ~Str();

  Str(const Str& from);
  Str(Str&& from) noexcept
    : Str() {
    *this = ::std::move(from);
  }

  inline Str& operator=(const Str& from) {
    CopyFrom(from);
    return *this;
  }
  inline Str& operator=(Str&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const Str& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Str* internal_default_instance() {
    return reinterpret_cast<const Str*>(
               &_Str_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    3;

  friend void swap(Str& a, Str& b) {
    a.Swap(&b);
  }
  inline void Swap(Str* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Str* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Str* New() const final {
    return CreateMaybeMessage<Str>(nullptr);
  }

  Str* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Str>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const Str& from);
  void MergeFrom(const Str& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Str* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "et.proto.Str";
  }
  protected:
  explicit Str(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_basic_2eproto);
    return ::descriptor_table_basic_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kValFieldNumber = 1,
  };
  // string val = 1;
  void clear_val();
  const std::string& val() const;
  void set_val(const std::string& value);
  void set_val(std::string&& value);
  void set_val(const char* value);
  void set_val(const char* value, size_t size);
  std::string* mutable_val();
  std::string* release_val();
  void set_allocated_val(std::string* val);
  GOOGLE_PROTOBUF_RUNTIME_DEPRECATED("The unsafe_arena_ accessors for"
  "    string fields are deprecated and will be removed in a"
  "    future release.")
  std::string* unsafe_arena_release_val();
  GOOGLE_PROTOBUF_RUNTIME_DEPRECATED("The unsafe_arena_ accessors for"
  "    string fields are deprecated and will be removed in a"
  "    future release.")
  void unsafe_arena_set_allocated_val(
      std::string* val);
  private:
  const std::string& _internal_val() const;
  void _internal_set_val(const std::string& value);
  std::string* _internal_mutable_val();
  public:

  // @@protoc_insertion_point(class_scope:et.proto.Str)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr val_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_basic_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// Bool

// bool val = 1;
inline void Bool::clear_val() {
  val_ = false;
}
inline bool Bool::_internal_val() const {
  return val_;
}
inline bool Bool::val() const {
  // @@protoc_insertion_point(field_get:et.proto.Bool.val)
  return _internal_val();
}
inline void Bool::_internal_set_val(bool value) {
  
  val_ = value;
}
inline void Bool::set_val(bool value) {
  _internal_set_val(value);
  // @@protoc_insertion_point(field_set:et.proto.Bool.val)
}

// -------------------------------------------------------------------

// Int

// int32 val = 1;
inline void Int::clear_val() {
  val_ = 0;
}
inline ::PROTOBUF_NAMESPACE_ID::int32 Int::_internal_val() const {
  return val_;
}
inline ::PROTOBUF_NAMESPACE_ID::int32 Int::val() const {
  // @@protoc_insertion_point(field_get:et.proto.Int.val)
  return _internal_val();
}
inline void Int::_internal_set_val(::PROTOBUF_NAMESPACE_ID::int32 value) {
  
  val_ = value;
}
inline void Int::set_val(::PROTOBUF_NAMESPACE_ID::int32 value) {
  _internal_set_val(value);
  // @@protoc_insertion_point(field_set:et.proto.Int.val)
}

// -------------------------------------------------------------------

// Double

// double val = 1;
inline void Double::clear_val() {
  val_ = 0;
}
inline double Double::_internal_val() const {
  return val_;
}
inline double Double::val() const {
  // @@protoc_insertion_point(field_get:et.proto.Double.val)
  return _internal_val();
}
inline void Double::_internal_set_val(double value) {
  
  val_ = value;
}
inline void Double::set_val(double value) {
  _internal_set_val(value);
  // @@protoc_insertion_point(field_set:et.proto.Double.val)
}

// -------------------------------------------------------------------

// Str

// string val = 1;
inline void Str::clear_val() {
  val_.ClearToEmpty(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
}
inline const std::string& Str::val() const {
  // @@protoc_insertion_point(field_get:et.proto.Str.val)
  return _internal_val();
}
inline void Str::set_val(const std::string& value) {
  _internal_set_val(value);
  // @@protoc_insertion_point(field_set:et.proto.Str.val)
}
inline std::string* Str::mutable_val() {
  // @@protoc_insertion_point(field_mutable:et.proto.Str.val)
  return _internal_mutable_val();
}
inline const std::string& Str::_internal_val() const {
  return val_.Get();
}
inline void Str::_internal_set_val(const std::string& value) {
  
  val_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value, GetArena());
}
inline void Str::set_val(std::string&& value) {
  
  val_.Set(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value), GetArena());
  // @@protoc_insertion_point(field_set_rvalue:et.proto.Str.val)
}
inline void Str::set_val(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  val_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value),
              GetArena());
  // @@protoc_insertion_point(field_set_char:et.proto.Str.val)
}
inline void Str::set_val(const char* value,
    size_t size) {
  
  val_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(
      reinterpret_cast<const char*>(value), size), GetArena());
  // @@protoc_insertion_point(field_set_pointer:et.proto.Str.val)
}
inline std::string* Str::_internal_mutable_val() {
  
  return val_.Mutable(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
}
inline std::string* Str::release_val() {
  // @@protoc_insertion_point(field_release:et.proto.Str.val)
  return val_.Release(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
}
inline void Str::set_allocated_val(std::string* val) {
  if (val != nullptr) {
    
  } else {
    
  }
  val_.SetAllocated(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), val,
      GetArena());
  // @@protoc_insertion_point(field_set_allocated:et.proto.Str.val)
}
inline std::string* Str::unsafe_arena_release_val() {
  // @@protoc_insertion_point(field_unsafe_arena_release:et.proto.Str.val)
  GOOGLE_DCHECK(GetArena() != nullptr);
  
  return val_.UnsafeArenaRelease(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      GetArena());
}
inline void Str::unsafe_arena_set_allocated_val(
    std::string* val) {
  GOOGLE_DCHECK(GetArena() != nullptr);
  if (val != nullptr) {
    
  } else {
    
  }
  val_.UnsafeArenaSetAllocated(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      val, GetArena());
  // @@protoc_insertion_point(field_unsafe_arena_set_allocated:et.proto.Str.val)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------

// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace proto
}  // namespace et

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_basic_2eproto
