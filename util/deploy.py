#!/usr/bin/env python3

import subprocess
import os
import paramiko

class Deployer():
    def __int__(self):
        pass

    @staticmethod
    def send(username="trevor", host="trevor1.local"):
        ws_dir = os.path.join(os.path.dirname(__file__), os.path.pardir)
        result = subprocess.run([
                           "rsync -ravP --exclude-from='.gitignore' --exclude '.git*' ../trevor_ws  " + username + "@" + host + ":~/ --delete"],
                            cwd=ws_dir,
                            shell=True,
                            capture_output=True,
                            text=True)

        print(result.stdout)

        return result.stdout

    @staticmethod
    def build(username: object = "trevor", host: object = "trevor1.local") -> object:
        print("building...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password="bathyopossum")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source /opt/ros/foxy/setup.bash; cd trevor_ws; colcon build --symlink-install")

        out = ""
        def line_buffered(f):
            line_buf = ""
            while not f.channel.exit_status_ready():
                line_buf += f.read(1).decode("utf-8")
                if line_buf.endswith('\n'):
                    yield line_buf
                    line_buf = ''

        for l in line_buffered(ssh_stdout):
            print(l)
            out += l

        return out

    @staticmethod
    def deploy(username="trevor", host="trevor1.local"):
        """sends source code and compiles on selected vehicle"""
        return  Deployer.send(username, host) + Deployer.build(username, host)




def main():
    Deployer.deploy()
    return

if __name__ == '__main__':
    main()

