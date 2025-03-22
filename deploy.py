import os
import requests
import subprocess
import time

def deploy(deploy_path):
    # change current path to the path of the script
    os.chdir(deploy_path)

    # execute command "s" in the shell and wait for finish
    cmd = "s deploy --type code -a aliyun-ram-account"
    subprocess.check_call(cmd, shell=True)

current_path = os.path.dirname(os.path.abspath(__file__))
deploy(os.path.join(current_path))
