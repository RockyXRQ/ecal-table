#include <chrono>
#include <iostream>
#include <thread>

#include "core.h"
#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    et::Table table(argc, argv, "rec_cb");

    table.entry<et::proto::Int>("test_int").setCallback([](const std::string &, const google::protobuf::Message &msg, double)
                                                        { std::cout << "int: " << dynamic_cast<const et::proto::Int &>(msg).val() << std::endl; });
    table.entry<et::proto::Double>("test_double").setCallback([](const std::string &, const google::protobuf::Message &msg, double)
                                                              { std::cout << "double: " << dynamic_cast<const et::proto::Double &>(msg).val() << std::endl; });
    table.entry<et::proto::Str>("test_str").setCallback([](const std::string &, const google::protobuf::Message &msg, double)
                                                        { std::cout << "str: " << dynamic_cast<const et::proto::Str &>(msg).val() << std::endl; });
    table.entry<et::proto::Bool>("test_bool").setCallback([](const std::string &, const google::protobuf::Message &msg, double)
                                                          { std::cout << "bool: " << dynamic_cast<const et::proto::Bool &>(msg).val() << std::endl; });
    table.entry<et::proto::Example>("test_msg").setCallback([](const std::string &, const google::protobuf::Message &msg, double)
                                                            { std::cout << "example: " << msg.DebugString() << std::endl; });
    try
    {
        while (table.ok())
        {
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
