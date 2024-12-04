find proto/ -name "*.py" -type f -delete

protoc --proto_path=proto/src --python_out=proto proto/src/*.proto
