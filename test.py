import os
import subprocess

var = os.environ['AWS_PROFILE'] = 'xxxx'
print(var)
cmd = subprocess.getoutput('export AWS_PROFILE="TEST"')
print(cmd)