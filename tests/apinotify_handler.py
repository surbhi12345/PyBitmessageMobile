#!/usr/bin/env python

import sys
import tempfile
from test_process import put_signal_file


if __name__ == '__main__':
    if sys.argv[1] == 'startingUp':
        put_signal_file(tempfile.gettempdir(), '.api_started')