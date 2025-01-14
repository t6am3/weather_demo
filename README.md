启动命令：
nohup uvicorn main:app --host 0.0.0.0 --port 12350 > run.log 2>&1 &

如需公网访问 可能需要增加代理，大家需要自己去查找下相关的资料
