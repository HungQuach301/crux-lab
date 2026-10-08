#!/usr/bin/env bash
set -uo pipefail
cd "/home/user/crux-lab/tongket-t5/indicators/frames"
[ -s R1.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh prompt-R1.txt R1.json --read || echo "LỖI R1.json"
[ -s R2.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh prompt-R2.txt R2.json --read || echo "LỖI R2.json"
[ -s R3.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh prompt-R3.txt R3.json --read || echo "LỖI R3.json"
