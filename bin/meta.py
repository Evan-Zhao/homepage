#!/usr/bin/env python3
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.timestamp import TimeStamp
from sys import argv
from datetime import datetime
from typing import Iterable, List
from os.path import getmtime


class MyYAML(YAML):
    def dump_to_str(self, data, **kwargs):
        stream = StringIO()
        YAML.dump(self, data, stream, **kwargs)
        return stream.getvalue()

    def dump_all_to_str(self, data, **kwargs):
        stream = StringIO()
        YAML.dump_all(self, data, stream, **kwargs)
        return stream.getvalue()


yaml = MyYAML()
yaml.explicit_start = True
yaml.indent(2)
yaml.preserve_quotes = True


def split_at(pred, xs: List):
    from itertools import takewhile, dropwhile, islice
    def not_pred(x): return not pred(x)
    left = list(takewhile(not_pred, xs))
    splitter = xs[len(left)]
    right = xs[len(left) + 1:]
    return left, splitter, right


class ParsedFile:
    def __init__(self, metadata: CommentedMap, pre_text: str, post_text: str):
        self._metadata = metadata
        self._pre_text = pre_text
        self._post_text = post_text

    def __repr__(self) -> str:
        return self._pre_text + yaml.dump_to_str(self._metadata) + self._post_text

    @classmethod
    def from_file(cls, path: Path) -> 'ParsedFile':
        def is_sep(s): return s == '---\n'
        with path.open() as fp:
            lines = fp.readlines()
        before, sep1, at_meta_begin = split_at(is_sep, lines)
        meta, sep2, after_meta = split_at(is_sep, at_meta_begin)
        meta_str = sep1 + ''.join(meta)
        data = yaml.load(meta_str)
        pre_text = ''.join(before)
        post_text = sep2 + ''.join(after_meta)
        return cls(data, pre_text, post_text)

    def rget(self, attr: str, default=None):
        def _get(obj_: dict, attr_: str):
            return obj_.get(attr_, default)

        import functools
        return functools.reduce(_get, attr.split('.'), self._metadata)

    def __contains__(self, attr: str):
        return self.rget(attr) is not None

    def __getitem__(self, attr: str):
        def _get(obj_: dict, attr_: str):
            return obj_[attr_]

        import functools
        return functools.reduce(_get, attr.split('.'), self._metadata)

    def __setitem__(self, attr: str, val):
        pre, _, post = attr.rpartition('.')
        parent = self[pre] if pre else self._metadata
        parent[post] = val

    def to_file_path(self, path: Path):
        with path.open('w') as fp:
            fp.write(self._pre_text)
            yaml.dump(self._metadata, fp)
            fp.write(self._post_text)


def get_file_mod_datetime_str(filename: str):
    from pytz import reference
    mtime_secs = getmtime(filename)
    mtime = datetime.utcfromtimestamp(mtime_secs)
    localtime = reference.LocalTimezone()
    mtime_tz = mtime.replace(tzinfo=localtime)
    return mtime_tz.strftime(r'%Y-%m-%dT%H:%M:%S%z')


if __name__ == "__main__":
    for filepath in argv[1:]:
        filepath = Path(filepath)
        if filepath.suffix != '.md' or not filepath.is_file():
            continue
        print(f"Processing {filepath}")
        input_meta = ParsedFile.from_file(filepath)
        if 'lastmod' in input_meta:
            input_meta['lastmod'] = get_file_mod_datetime_str(argv[1])
        input_meta.to_file_path(filepath)
