Для генерации ssl
<code>
pip install -r requirements.txt <br>
mkdir keys <br>
сd keys<br>
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
</code>

if need gen grpc service 
command: python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. *.proto





