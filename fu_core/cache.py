#!/usr/bin/env python2

################################################################################
# Name     : cache.py                                                          #
# Brief    : Fu can be really slow, local cache is necessary with 2 requires.  #
#             1. show local results directly, if there are.                    #
#             2. update results, when it is possible (backend)                 #
#                                                                              #
# Url      : http://stackoverflow.com/questions/3358770/                       #
#                   python-dictionary-is-thread-safe                           #
# Author   : Chunqi SHI <diligence.cs@gmail.com>                               #
################################################################################

import time, sys, os
# from os.path import expanduser
import cPickle as pickle


def pkl_dump(obj, pklfile):
    if os.path.exists(os.path.dirname(pklfile)):
        fp = open(pklfile, 'wb')
        try:
            pickle.dump(obj, fp)
        except IOError as err:
            pass
        finally:
            fp.close()

def pkl_load(pklfile):
    if os.path.exists(pklfile):
        fp = open(pklfile, 'rb')
        try:
            return pickle.load(fp)
        except IOError as err:
            # print err
            pass
        finally:
            fp.close()


class TimedResultDict(object):
    ### default 1 week, since web site will not update a lot between 1 week. ###
    def __init__(self, outdaterange=604800, pickfile='.fu_cached_pickle'):
        ### query:(result, time) map ###
        self.resultdict = {}
        self.outdaterange = outdaterange
        ### self.outdaterange = 5 ### Test
        ### http://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python ###
        self.pickfile = os.path.abspath(os.path.join(os.path.expanduser('~'), pickfile))

    @staticmethod
    def load(pickfile='.fu_cached_pickle'):
        pickfile = os.path.abspath(os.path.join(os.path.expanduser('~'), pickfile))
        trd = pkl_load(pickfile)
        if trd is None:
            trd = TimedResultDict(pickfile)
        else:
            trd.pickfile = pickfile
        return trd

    def dump(self):
        pkl_dump(self,self.pickfile)

    def is_outdate(self, querytime):
        return time.time() - querytime > self.outdaterange

    def put(self, query, result):
        ### only if valid result (simple test) ###
        if sys.getsizeof(result) > 21:
            self.resultdict[query] = result

    def get_and_update(self, query, func_update, *args, **kwargs):
        rst = self.get(query)
        if rst is None:
            rst = func_update(*args, **kwargs)
            self.put(query, (rst, time.time()))
            ### put and dump
            self.dump()
        return rst

    def get(self, query):
        if self.resultdict.has_key(query):
            (res, tim) = self.resultdict[query]
            if self.is_outdate(tim):
                return None
            else:
                return res
        else:
            return None



