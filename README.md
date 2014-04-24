Enter your GRAPHITE_URL into secrets.py like this:

GRAPHITE_URL=example.graphite.com

This script will capture your DOWN keystrokes. Every time you press a key, it will increment a counter that gets sent to graphite. This could be useful for overlaying with something like a GitHub commit to see keystroke activity increase / decrease before and after commits.

The script does not send any key logging data or collect any beyond a simple "press down" event.