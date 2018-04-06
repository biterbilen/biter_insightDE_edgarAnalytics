"""
Main for Pq
"""
from __future__ import absolute_import

from sys import argv

from pq import Pq, Node

def main(f_log, f_inactivity, f_out):
    """main for Pq"""
    # define used f_log header fields
    fields = {'ip':'ip', 'date':'date', 'time':'time'}
    verbose = False
    with open(f_inactivity) as ifp:
        inactivity_period = int(ifp.readline().rstrip())
    sess = Pq(inactivity_period, f_out, verbose=verbose)
    with open(f_log) as ifp:
        header = ifp.readline().rstrip().split(",")
        puser = None
        for user in ifp:
            user = dict(zip(header, user.split(",")))
            user = Node(user[fields['ip']],
                        user[fields['date']],
                        user[fields['time']])
            if puser != None and puser.sdt != user.sdt:
                sess.remove(user)
            sess.insert(user)
            puser = user
        sess.remove()

if __name__ == "__main__":
    main(argv[1], argv[2], argv[3])
