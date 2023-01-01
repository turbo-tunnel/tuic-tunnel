# -*- coding: utf-8 -*-

import asyncio
import os
import platform
import random
import subprocess
import sys

import turbo_tunnel


class TUICTunnel(turbo_tunnel.socks.Socks5Tunnel):
    """TUIC Tunnel"""

    tuic_process = None
    tuic_local_port = random.randint(10000, 20000)

    def __init__(self, tunnel, url=None, address=None, server_side=False):
        url = turbo_tunnel.utils.Url(
            "socks5://127.0.0.1:%d" % self.__class__.tuic_local_port
        )
        super(TUICTunnel, self).__init__(tunnel, url, address, server_side)

    @classmethod
    async def get_tunnel_address(cls, url):
        if cls.tuic_process is None:
            cls.tuic_process = await cls.start_tuic_process(
                url.address, url.auth, cls.tuic_local_port
            )
            turbo_tunnel.utils.logger.info(
                "[%s] TUIC process id is %d" % (cls.__name__, cls.tuic_process.pid)
            )
        return ("127.0.0.1", cls.tuic_local_port)

    @classmethod
    async def start_tuic_process(cls, server, token, listen_port):
        current_path = os.path.dirname(os.path.abspath(__file__))
        bin_path = os.path.join(
            current_path, "bin", sys.platform, "tuic-client-%s" % platform.machine()
        )
        if sys.platform == "win32":
            bin_path += ".exe"
        if not os.path.isfile(bin_path):
            raise RuntimeError("File %s not exist" % bin_path)
        if sys.platform != "win32":
            os.chmod(bin_path, 0o755)
        cmdline = (
            "%s --server=%s --server-port=%d --token=%s --local-port=%d --alpn=h3"
            % (bin_path, server[0], server[1], token, listen_port)
        )
        if sys.platform != "win32":
            return await asyncio.create_subprocess_shell(cmdline)
        else:
            return subprocess.Popen(cmdline)


turbo_tunnel.registry.tunnel_registry.register("tuic", TUICTunnel)
