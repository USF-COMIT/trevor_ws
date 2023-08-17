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

        return result.stdout

    @staticmethod
    def build(username: object = "trevor", host: object = "trevor1.local") -> object:
        print("building...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password="bathyopossum")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source /opt/ros/foxy/setup.bash; cd trevor_ws; colcon build")
        cmd_output = ssh_stdout.read()
        print('log printing: ', cmd_output)
        return cmd_output.decode("utf-8")

    @staticmethod
    def deploy(username="trevor", host="trevor1.local"):
        """sends source code and compiles on selected vehicle"""
        return  Deployer.send(username, host) + Deployer.build(username, host)




def main():
    Deployer.deploy()
    return

if __name__ == '__main__':
    main()

