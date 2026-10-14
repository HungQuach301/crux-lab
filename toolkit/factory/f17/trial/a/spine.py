"""F-17 thử · đoạn a-s01-s03 của Tập 7."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
import spine_trial  # noqa: E402
CINE = json.loads("{\"look\": \"day\", \"shots\": {\"s4\": {\"shot\": \"close\", \"focus\": \"char\", \"aperture\": 0.9, \"override\": {\"keyAz\": 160, \"keyEl\": 30}}}}")
spine_trial.write(HERE, 'a-s01-s03', CINE)
