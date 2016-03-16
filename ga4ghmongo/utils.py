import os
import hashlib
import re
import json



def make_hash(s):
    return hashlib.sha256(s.encode("ascii", errors="ignore")).hexdigest()


def make_var_hash(ref, pos, alts):
    var = "".join(
        [ref, str(pos), "/".join(alts)])
    return make_hash(var)


def split_var_name(name):
    items = re.match(r"([A-Z]+)([-0-9]+)([A-Z/]+)", name, re.I).groups()
    return items[0], int(items[1]), items[2]


def unique(l):
    seen = set()
    return [x for x in l if x not in seen and not seen.add(x)]


def flatten(l):
    return [item for sublist in l for item in sublist]


