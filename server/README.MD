## 概述
视频直播服务器使用nodejs语言编程，通过http服务接受推流端数据，然后通过websocket连接广播到客户端。

## 启动方式

### Linux
```bash
node websocket-relay.js 10001 10002 &
```

### Window Server