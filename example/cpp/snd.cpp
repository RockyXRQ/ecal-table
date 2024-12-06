#include <chrono>
#include <iostream>
#include <thread>

#include "core.h"
#include "proto/cpp/basic.pb.h"
#include "proto/cpp/example.pb.h"

int main(int argc, char **argv)
{
    et::Table table(argc, argv, "snd");

    // 初始化值
    int int_val = 1;
    double double_val = 2.0;
    std::string str_val = "Hello";
    bool bool_val = true;
    et::proto::Example example_msg;
    example_msg.set_val_1("LALALA");
    example_msg.set_val_2(32123);

    try
    {
        while (table.ok())
        {
            et::proto::Int int_msg;
            int_msg.set_val(int_val);
            table.entry<et::proto::Int>("test_int").set(int_msg);

            et::proto::Double double_msg;
            double_msg.set_val(double_val);
            table.entry<et::proto::Double>("test_double").set(double_msg);

            et::proto::Str str_msg;
            str_msg.set_val(str_val);
            table.entry<et::proto::Str>("test_str").set(str_msg);

            et::proto::Bool bool_msg;
            bool_msg.set_val(bool_val);
            table.entry<et::proto::Bool>("test_bool").set(bool_msg);

            table.entry<et::proto::Example>("test_msg").set(example_msg);

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
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
