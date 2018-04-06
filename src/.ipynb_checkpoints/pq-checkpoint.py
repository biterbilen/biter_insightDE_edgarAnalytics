"""
OrderedDict with timeout(Pq)
"""
from __future__ import absolute_import

from collections import OrderedDict

from datetime import datetime, date, time

class Node(object):
    """Represents a user session"""
    def __init__(self, uip, dat, tim):
        self.uip = uip
        self.sdt = datetime.combine(date(*map(int, dat.split("-"))),
                                    time(*map(int, tim.split(":"))))
        self.fdt = self.sdt
        self.ndur = (self.fdt - self.sdt).total_seconds()
        self.nreq = 1
    def __repr__(self):
        return "%s,%s,%s,%d,%d" % \
            (self.uip,
             self.sdt.strftime("%Y-%m-%d %H:%M:%S"),
             self.fdt.strftime("%Y-%m-%d %H:%M:%S"),
             (self.fdt - self.sdt).total_seconds() + 1, #inclusive
             self.nreq)
    __str__ = __repr__

class Pq(object):
    """Represents a OrderedDict w/timeout"""
    def __init__(self, timeout, ofile, verbose=False):
        self.nodes = OrderedDict()
        self.timeout = timeout
        self.verbose = verbose
        self.ofp = open(ofile, "w")
    def __exit__(self, ex_type, ex_value, traceback):
        self.ofp.close()
    def __repr__(self):
        return "\n".join(["%s" % val for val in self.nodes.values()])
    __str__ = __repr__
    def insert(self, obj):
        """Inserts an entry or modifies its fields if it already exists"""
        if self.verbose:
            print __name__
        if obj.uip in self.nodes.keys():
            self.nodes[obj.uip].fdt = obj.fdt
            self.nodes[obj.uip].nreq += 1
        else:
            self.nodes.update({obj.uip:obj})
    def remove(self, obj=None):
        """Removes/Outputs entries w/timeout"""
        if self.verbose:
            print __name__
        for key, val in self.nodes.iteritems():
            if obj is not None:
                ndur = (obj.fdt - val.fdt).total_seconds()
                if self.verbose:
                    print key, ndur
                if ndur <= self.timeout:
                    continue
            self.ofp.write(str(val) + "\n")
            del self.nodes[key]
