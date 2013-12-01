# -*- coding: utf-8 -*-
from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Apt(BaseAdapter):
    """
    apt-get adapter
    """
    search_command = 'apt-cache'

    def adapter_command(self):
        return 'apt-get'

    def search(self, query):
        response = self._execute_command(self.search_command, ['search', query])[0].decode(*enc)
        regex = re.compile('^([^ ]*) - (.*)')
        return { 'apt:'+m.group(1): m.group(2) for m in map(regex.match, response.splitlines()) if m }

    def info(self, query):
        response = self._execute_command(self.search_command, ['show', query])[0].decode(*enc)
        return self.munge_lines([(a, b) for a, _, b in map(lambda s: s.rpartition(': '), response.splitlines)])

    def install(self, query):
        return self.shell('install', query)
