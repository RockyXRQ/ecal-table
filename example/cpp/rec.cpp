#include <chrono>
#include <iostream>
#include <thread>

#include "core.h"
#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    et::Table table(argc, argv, "rec");

    try
    {
        while (table.ok())
        {
            et::proto::Int default_int;
            default_int.set_val(0);
            std::cout << "int: " << table.entry<et::proto::Int>("test_int").get(default_int).DebugString() << std::endl;

            et::proto::Double default_double;
            default_double.set_val(0.0);
            std::cout << "double: " << table.entry<et::proto::Double>("test_double").get(default_double).DebugString() << std::endl;

            et::proto::Str default_str;
            default_str.set_val("");
            std::cout << "str: " << table.entry<et::proto::Str>("test_str").get(default_str).DebugString() << std::endl;

            et::proto::Bool default_bool;
            default_bool.set_val(false);
            std::cout << "bool: " << table.entry<et::proto::Bool>("test_bool").get(default_bool).DebugString() << std::endl;

            et::proto::Example default_example;
            default_example.set_val_1("xixixi");
            default_example.set_val_2(12321);
            std::cout << "example: " << table.entry<et::proto::Example>("test_msg").get(default_example).DebugString() << std::endl;
            std::cout << std::endl;

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
