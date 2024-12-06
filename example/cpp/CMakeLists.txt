cmake_minimum_required(VERSION 3.10)
project(ecal_table_examples)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(eCAL REQUIRED)
find_package(Protobuf REQUIRED)

# 添加 protobuf 生成的源文件
add_library(proto_lib
    ${CMAKE_SOURCE_DIR}/../../proto/cpp/basic.pb.cc
    ${CMAKE_SOURCE_DIR}/../../proto/cpp/example.pb.cc
)

target_link_libraries(proto_lib
    PUBLIC
    protobuf::libprotobuf
)

add_executable(snd snd.cpp)
add_executable(rec rec.cpp)
add_executable(rec_cb rec_cb.cpp)

include_directories(
    ${CMAKE_SOURCE_DIR}/../../
    ${CMAKE_SOURCE_DIR}/../../proto/cpp
    ${PROTOBUF_INCLUDE_DIRS}
)

foreach(target snd rec rec_cb)
    target_link_libraries(${target}
        PRIVATE
        eCAL::core
        proto_lib
    )
endforeach() 
