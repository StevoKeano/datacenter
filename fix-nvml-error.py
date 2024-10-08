import json
import pathlib
import subprocess
import sys
```
=> Begin vast host software install
=> Configure Vast.ai daemon
=> Update Vast.ai daemon
=> Install docker
=> Install docker
=> check apt update
=> check apt update
=> Test docker
Using default tag: latest
latest: Pulling from library/ubuntu
Digest: sha256:dfc10878be8d8fc9c61cbff33166cb1d1fe44391539243703c72766894fa834a
Status: Image is up to date for ubuntu:latest
docker.io/library/ubuntu:latest
    Testing nvidia-docker for NVML error (30 seconds)
NVML test failed!

```
supported_versions = ['22.04', '24.04']

if not any(e in subprocess.run(['lsb_release', '-r'], check=True, stdout=subprocess.PIPE).stdout.decode() for e in supported_versions):
    print(f"Your ubuntu version is not supported. The following versions are supported: {supported_versions}")
    sys.exit()

json_path = pathlib.Path(r"/etc/docker/daemon.json")

if not json_path.is_file():
    print("Run vastai install script first.")
    sys.exit()

with json_path.open('r', encoding='utf-8') as f:
    json_dict = json.load(f) or {}

if 'exec-opts' in json_dict:
    print("No need to fix.")
    sys.exit()

json_dict['exec-opts'] = ["native.cgroupdriver=cgroupfs"]

with json_path.open('w', encoding='utf-8') as f:
    json.dump(json_dict, f, indent=4, sort_keys=True)

if subprocess.run(['sudo', 'systemctl', 'restart', 'docker'], check=True, stdout=subprocess.PIPE).returncode == 0:
    print("Docker service has been restarted.")

print("Complete. Run vastai install script again.")
