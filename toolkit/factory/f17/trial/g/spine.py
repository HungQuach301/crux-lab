"""F-17 thử · đoạn g-s29-s33 của Tập 7."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
import spine_trial  # noqa: E402
CINE = json.loads("{\"look\": \"dusk\"}")
spine_trial.write(HERE, 'g-s29-s33', CINE)
