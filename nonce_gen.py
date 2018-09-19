#!/usr/bin/env python

# Use this module to generate a 32bit none number

import os
import time
import random

def generate_nonce(length=32):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])
