"""F-17 thử · đoạn c-s10-s15 của Tập 7."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
import spine_trial  # noqa: E402
CINE = json.loads("{\"look\": \"afternoon\", \"sky\": 0}")
spine_trial.write(HERE, 'c-s10-s15', CINE)
