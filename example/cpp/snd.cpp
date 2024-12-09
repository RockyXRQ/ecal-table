#include <chrono>
#include <iostream>
#include <thread>
#include <ecal/ecal.h>
#include <ecal/msg/protobuf/publisher.h>

#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    eCAL::Initialize(argc, argv, "snd");

    auto intPub = eCAL::protobuf::CPublisher<et::proto::Int>("test_int");
    auto doublePub = eCAL::protobuf::CPublisher<et::proto::Double>("test_double");
    auto strPub = eCAL::protobuf::CPublisher<et::proto::Str>("test_str");
    auto boolPub = eCAL::protobuf::CPublisher<et::proto::Bool>("test_bool");
    auto examplePub = eCAL::protobuf::CPublisher<et::proto::Example>("test_msg");

    int int_val = 1;
    double double_val = 2.0;
    std::string str_val = "Hello";
    bool bool_val = true;
    et::proto::Example example_msg;
    example_msg.set_val_1("LALALA");
    example_msg.set_val_2(32123);

    while (eCAL::Ok())
    {
        et::proto::Int int_msg;
        int_msg.set_val(int_val);
        intPub.Send(int_msg);

        et::proto::Double double_msg;
        double_msg.set_val(double_val);
        doublePub.Send(double_msg);

        et::proto::Str str_msg;
        str_msg.set_val(str_val);
        strPub.Send(str_msg);

        et::proto::Bool bool_msg;
        bool_msg.set_val(bool_val);
        boolPub.Send(bool_msg);

        examplePub.Send(example_msg);

        std::cout << "int: " << int_val << std::endl;
        std::cout << "double: " << double_val << std::endl;
        std::cout << "str: " << str_val << std::endl;
        std::cout << "bool: " << bool_val << std::endl;
        std::cout << "example: " << example_msg.DebugString() << std::endl;
        std::cout << std::endl;

        int_val++;
        double_val += 1.0;
        str_val += "!";
        bool_val = !bool_val;

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    eCAL::Finalize();
    return 0;
}
