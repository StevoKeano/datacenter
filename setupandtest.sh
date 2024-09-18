# https://github.com/jjziets/vasttools/blob/main/README.md#self-verification-test
wget https://raw.githubusercontent.com/vast-ai/vast-python/master/vast.py -O vast
chmod +x vast
./vast set api-key 2fa5b7c8ebb62b387b5a51c1c9abe25fb8beeda129f5f24f88b096460a6e0e5e

wget https://github.com/jjziets/VastVerification/releases/download/0.4-beta/autoverify_machineid.sh
chmod +x autoverify_machineid.sh
sudo apt update
sudo apt install bc jq
 ./autoverify_machineid.sh 27980
./autoverify_machineid.sh --ignore-requirements   27980

