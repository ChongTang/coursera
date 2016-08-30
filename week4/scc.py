"""
enlarge your stack size with 'ulimit -s 131072' before run
"""
import random
import copy
import time
import sys

random.seed(int(time.time()))
sys.setrecursionlimit(3000000)


class kosaraju(object):
    '''
    Kosaraju's Two-Pass Algorithm
    '''
    def __init__(self, f):
        '''
        Argo1: directed graph file metioned by adjacency list
        '''
        self.G = {}
        self.Grev = {}
        self.v_latest = 0

        #caculated G, Grev, and lastest V
        with open(f, 'r') as f:
            for line in f.readlines():
                u, v = map(int, line.replace('\n', '').replace('\r', '').split())
                if self.v_latest < u: self.v_latest = u # figure bigest number of node out
                self.G.setdefault(u, []).append(v)
                self.Grev.setdefault(v, []).append(u)

        self.t_g = 0 # number of nodes processed so far
        self.s_g = 0 # current source vertex
        self.explored = [ 0 for i in range(self.v_latest+1) ]
        self.leader   = [ 0 for i in range(self.v_latest+1) ]
        self.finish   = [ 0 for i in range(self.v_latest+1) ]


    def _stack_clean(self):
        self.t_g = 0 # number of nodes processed so far
        self.s_g = 0 # current source vertex
        self.explored = [ 0 for i in range(self.v_latest+1) ]
        self.leader   = [ 0 for i in range(self.v_latest+1) ]
        self.finish   = [ 0 for i in range(self.v_latest+1) ]


    def _dfs(self, G, i):
        self.explored[i] = 1
        self.leader[i] = self.s_g

        if G.get(i):
            for adj in G[i]:
                if not self.explored[adj]:
                    self._dfs(G, adj)

        self.t_g+=1
        self.finish[i] = self.t_g


    def _dfs_loop(self, G):
        # first DFS-Loop
        self._stack_clean()

        for i in range(self.v_latest, 0, -1):
            if not self.explored[i]:
                self.s_g = i
                self._dfs(G, i)

        self.explored.pop(0)
        self.leader.pop(0)
        self.finish.pop(0)


    def _build_g_scc(self, G, f):
        f_map = {}
        Gscc = {}

        for i in range(len(f)):
            f_map[i] = f[i]

        for u, adjs in G.items():
            Gscc[f_map[u-1]] = [ f_map[i-1] for i in adjs ]

        return Gscc


    def get_scc_stats(self):
        scc_leader = {}
        courser_fmt = []

        for i in self.leader:
            if not scc_leader.get(i): scc_leader.setdefault(i, 0)
            scc_leader[i] = scc_leader[i]+1

        for i in scc_leader:
            courser_fmt.append(scc_leader[i])

        courser_fmt = sorted(courser_fmt)
        courser_fmt.reverse()
        if len(scc_leader) < 5:
            [ courser_fmt.append(0) for i in range(5-len(scc_leader))]

        return courser_fmt[:5]


    def show_scc_stats(self):
        scc_leader = {}

        for i in self.leader:
            if not scc_leader.get(i): scc_leader.setdefault(i, 0)
            scc_leader[i] = scc_leader[i]+1


    def run(self, verbose = False):
        self._dfs_loop(self.Grev)
        if verbose: self.show_stats()

        # build Gscc
        Gscc = self._build_g_scc(self.G, self.finish)
        #  draw_graph(Gscc, True)
        self._dfs_loop(Gscc)
        if verbose: self.show_stats()

        if verbose: self.show_scc_stats()

def main():
    test_data = 'SCC.txt'
    ans = (\
            [3, 3, 3, 0, 0], \
            [3, 3, 2, 0, 0], \
            [3, 3, 1, 1, 0], \
            [7, 1, 0, 0, 0], \
            [6, 3, 2, 1, 0], \
            [434821, 968, 459, 313, 211], \
            )

    sys.stdout.write(test_data)
    ksj = kosaraju(test_data)
    ksj.run()
    sys.stdout.write(str(ksj.get_scc_stats()) + ' ')
    print(ksj.get_scc_stats() == ans[0])

if __name__ == '__main__':
    main()
