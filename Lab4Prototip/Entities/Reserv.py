class Reservierung:
    def __init__(self, zimmer, nrg, ci, co):
        self.__zimmer = zimmer
        self.__nrg = nrg
        self.__ci = ci
        self.__co = co

    """def __str__(self):
        return "{};{};{};{}".format(self.zimmer, self.nrg, self.ci, self.co)"""

    def __repr__(self):
        return "{};{};{};{}".format(self.zimmer, self.nrg, self.ci, self.co)

    def __eq__(self, other):
        return self.zimmer == other.zimmer and self.nrg == other.nrg and self.ci == other.ci and self.co == other.co

    @property
    def co(self): return self.__co

    @co.setter
    def co(self, co): self.__co = co

    @property
    def ci(self): return self.__ci

    @ci.setter
    def ci(self, ci): self.__ci = ci

    @property
    def nrg(self): return self.__nrg

    @nrg.setter
    def nrg(self, nrg): self.__nrg = nrg

    @property
    def zimmer(self): return self.__zimmer

    @zimmer.setter
    def zimmer(self, zimmer): self.__zimmer = zimmer
