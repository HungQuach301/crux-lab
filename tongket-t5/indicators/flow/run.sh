#!/usr/bin/env bash
set -uo pipefail
cd "/home/user/crux-lab/tongket-t5/indicators/flow"
[ -s 3571cd18/R1.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 3571cd18/prompt-R1.txt 3571cd18/R1.json --read || echo "LỖI 3571cd18/R1.json"
[ -s 3571cd18/R2.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 3571cd18/prompt-R2.txt 3571cd18/R2.json --read || echo "LỖI 3571cd18/R2.json"
[ -s 3571cd18/R3.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 3571cd18/prompt-R3.txt 3571cd18/R3.json --read || echo "LỖI 3571cd18/R3.json"
[ -s 55aa8f78/R1.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 55aa8f78/prompt-R1.txt 55aa8f78/R1.json --read || echo "LỖI 55aa8f78/R1.json"
[ -s 55aa8f78/R2.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 55aa8f78/prompt-R2.txt 55aa8f78/R2.json --read || echo "LỖI 55aa8f78/R2.json"
[ -s 55aa8f78/R3.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 55aa8f78/prompt-R3.txt 55aa8f78/R3.json --read || echo "LỖI 55aa8f78/R3.json"
[ -s 50d3ea49/R1.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 50d3ea49/prompt-R1.txt 50d3ea49/R1.json --read || echo "LỖI 50d3ea49/R1.json"
[ -s 50d3ea49/R2.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 50d3ea49/prompt-R2.txt 50d3ea49/R2.json --read || echo "LỖI 50d3ea49/R2.json"
[ -s 50d3ea49/R3.json ] || bash /home/user/crux-lab/toolkit/blind/headless.sh 50d3ea49/prompt-R3.txt 50d3ea49/R3.json --read || echo "LỖI 50d3ea49/R3.json"
