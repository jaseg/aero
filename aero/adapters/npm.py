# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE
from string import strip
class Npm(BaseAdapter):
    adapter_command = 'npm'

    def search(self, query):
        response = Popen(self.adapter_command + ' search -q ' + query, shell=True, stdout=PIPE).communicate()[0]
        lst = list(self.__parse_search(line) for line in response.splitlines() if ' - ' in line)
        if lst:
            return dict(lst)
        return {}

    def __parse_search(self, result):
        return map(strip, (self.adapter_command + ':' + result).split(' - ', 1))

    def install(self, query):
        print '\n'
        Popen(self.adapter_command + ' install ' + query, shell=True).wait()
        return {}