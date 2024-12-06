CURRENT_DIR=$(pwd)

rm -rf proto/py proto/cpp
mkdir -p proto/py proto/cpp

protoc --proto_path=proto/src \
    --python_out=${CURRENT_DIR}/proto/py \
    --cpp_out=${CURRENT_DIR}/proto/cpp \
    proto/src/*.proto

init_file="proto/__init__.py"
for file in proto/src/*.proto; do
    filename=$(basename "$file" .proto)
    echo "from .py.${filename}_pb2 import *" >> "$init_file"
done
