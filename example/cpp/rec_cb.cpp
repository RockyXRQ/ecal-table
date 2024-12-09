#include <chrono>
#include <iostream>
#include <thread>
#include <ecal/ecal.h>
#include <ecal/msg/protobuf/subscriber.h>

#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    eCAL::Initialize(argc, argv, "rec_cb");

    auto intSub = eCAL::protobuf::CSubscriber<et::proto::Int>("test_int");
    auto doubleSub = eCAL::protobuf::CSubscriber<et::proto::Double>("test_double");
    auto strSub = eCAL::protobuf::CSubscriber<et::proto::Str>("test_str");
    auto boolSub = eCAL::protobuf::CSubscriber<et::proto::Bool>("test_bool");
    auto exampleSub = eCAL::protobuf::CSubscriber<et::proto::Example>("test_msg");

    intSub.AddReceiveCallback([](const char *topic_name_, const et::proto::Int &msg_, long long time_, long long clock_, long long id_)
                              { std::cout << "int: " << msg_.DebugString() << std::endl; });
    doubleSub.AddReceiveCallback([](const char *topic_name_, const et::proto::Double &msg_, long long time_, long long clock_, long long id_)
                                 { std::cout << "double: " << msg_.DebugString() << std::endl; });
    strSub.AddReceiveCallback([](const char *topic_name_, const et::proto::Str &msg_, long long time_, long long clock_, long long id_)
                              { std::cout << "str: " << msg_.DebugString() << std::endl; });
    boolSub.AddReceiveCallback([](const char *topic_name_, const et::proto::Bool &msg_, long long time_, long long clock_, long long id_)
                               { std::cout << "bool: " << msg_.DebugString() << std::endl; });
    exampleSub.AddReceiveCallback([](const char *topic_name_, const et::proto::Example &msg_, long long time_, long long clock_, long long id_)
                                  { std::cout << "example: " << msg_.DebugString() << std::endl; });
    while (eCAL::Ok())
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    eCAL::Finalize();
    return 0;
}
