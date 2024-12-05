find proto/ -name "*.py" -type f -delete

protoc --proto_path=proto/src --python_out=proto proto/src/*.proto

generate_init_py() {
    init_file="proto/__init__.py"
    for file in proto/src/*.proto; do
        filename=$(basename "$file" .proto)
        echo "from .${filename}_pb2 import *" >> "$init_file"
    done
}

generate_init_py
