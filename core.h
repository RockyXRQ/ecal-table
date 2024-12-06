#pragma once

#include <ecal/ecal.h>
#include <ecal/msg/protobuf/publisher.h>
#include <ecal/msg/protobuf/subscriber.h>
#include <google/protobuf/message.h>
#include <functional>
#include <memory>
#include <string>

namespace et
{
    template <typename T>
    class Entry
    {
    public:
        Entry(const std::string &key) : key_(key)
        {
        }

        void set(const T &msg)
        {
            lazyInitPub();
            pub_->Send(msg);
        }

        T get(const T &default_msg)
        {
            lazyInitSub();
            T val = default_msg;
            if (sub_->Receive(val))
            {
                return val;
            }
            return default_msg;
        }

        using CallbackType = std::function<void(const std::string &, const T &, double)>;
        void setCallback(CallbackType callback)
        {
            lazyInitSub();
            sub_->AddReceiveCallback(
                [callback](const char *topic_name, const T &msg,
                           long long time, long long clock, long long id)
                {
                    callback(topic_name, msg, static_cast<double>(time) / 1e6);
                });
        }

        void removeCallback()
        {
            if (sub_)
            {
                sub_->RemReceiveCallback();
            }
        }

    private:
        void lazyInitPub()
        {
            if (!pub_)
            {
                pub_ = std::make_unique<eCAL::protobuf::CPublisher<T>>(key_);
            }
        }

        void lazyInitSub()
        {
            if (!sub_)
            {
                sub_ = std::make_unique<eCAL::protobuf::CSubscriber<T>>(key_);
            }
        }

        std::string key_;
        std::unique_ptr<eCAL::protobuf::CPublisher<T>> pub_;
        std::unique_ptr<eCAL::protobuf::CSubscriber<T>> sub_;
    };

    class Table
    {
    public:
        Table(int argc, char **argv, const std::string &name)
        {
            if (!has_ecal_init_)
            {
                has_ecal_init_ = true;
                eCAL::Initialize(argc, argv, name.c_str());
            }
        }

        ~Table()
        {
            if (has_ecal_init_)
            {
                eCAL::Finalize();
            }
        }

        bool ok() const { return eCAL::Ok(); }

        template <typename T>
        Entry<T> entry(const std::string &key)
        {
            return Entry<T>(key);
        }

    private:
        static inline bool has_ecal_init_ = false;
    };
} // namespace et
