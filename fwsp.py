import subprocess

subprocess.check_call('netsh advfirewall set allprofile state off')
