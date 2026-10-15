"""F-17 thử · đoạn a-s01-s03 của Tập 7 (đối chứng, không lớp)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
import spine_trial  # noqa: E402
CINE = json.loads("null")
spine_trial.write(HERE, 'a-s01-s03', CINE)
