# TUIC plugin for turbo-tunnel

## WHAT IS TUIC

[TUIC](https://github.com/EAimTY/tuic)is a high performance proxy based on QUIC protocol.

## INSTALL

```bash
$ pip3 install tuic-tunnel
```

## HOW TO USE

### Simple Usage

```bash
$ turbo-tunnel -l http://127.0.0.1:8888 -t tuic://token@proxy.com:8443 -p tuic_tunnel
```

`proxy.com:8443` is the `TUIC` server domain and udp port, `token` is the `TUIC` token.

### Use With Config File

```yaml
version: 1.0

listen: 
  - http://127.0.0.1:8888 # 配置监听地址

plugins:
  - tuic_tunnel

tunnels:
  - id: tuic
    url: tuic://token@proxy.com:8443/

rules:
  - id: tuic
    priority: 99
    addr: "*.baidu.com"
    port: 80;443;
    tunnel: tuic
```

```bash
$ turbo-tunnel -c config.yaml
```
