#include <chrono>
#include <iostream>
#include <thread>
#include <ecal/ecal.h>
#include <ecal/msg/protobuf/publisher.h>
#include <ecal/msg/protobuf/subscriber.h>

#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    eCAL::Initialize(argc, argv, "rec");

    auto intSub = eCAL::protobuf::CSubscriber<et::proto::Int>("test_int");
    auto doubleSub = eCAL::protobuf::CSubscriber<et::proto::Double>("test_double");
    auto strSub = eCAL::protobuf::CSubscriber<et::proto::Str>("test_str");
    auto boolSub = eCAL::protobuf::CSubscriber<et::proto::Bool>("test_bool");
    auto exampleSub = eCAL::protobuf::CSubscriber<et::proto::Example>("test_msg");

    auto intMsg = et::proto::Int();
    auto doubleMsg = et::proto::Double();
    auto strMsg = et::proto::Str();
    auto boolMsg = et::proto::Bool();
    auto exampleMsg = et::proto::Example();

    while (eCAL::Ok())
    {
        et::proto::Int default_int;
        default_int.set_val(0);
        intSub.Receive(intMsg);
        std::cout << "int: " << intMsg.DebugString() << std::endl;

        et::proto::Double default_double;
        default_double.set_val(0.0);
        doubleSub.Receive(doubleMsg);
        std::cout << "double: " << doubleMsg.DebugString() << std::endl;

        et::proto::Str default_str;
        default_str.set_val("");
        strSub.Receive(strMsg);
        std::cout << "str: " << strMsg.DebugString() << std::endl;

        et::proto::Bool default_bool;
        default_bool.set_val(false);
        boolSub.Receive(boolMsg);
        std::cout << "bool: " << boolMsg.DebugString() << std::endl;

        et::proto::Example default_example;
        default_example.set_val_1("xixixi");
        default_example.set_val_2(12321);
        exampleSub.Receive(exampleMsg);
        std::cout << "example: " << exampleMsg.DebugString() << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    eCAL::Finalize();

    return 0;
}
