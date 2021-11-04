class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        def dfs(prefix, _tiles):
            if prefix in res:
                return 
            print("prefix being added " + str(prefix))
            res.add(prefix)
            for i, t in enumerate(_tiles):
                print(i)
                print(t)
                print("prefix + t " + str(prefix + t))
                print("_tiles[:i] " + str(_tiles[:i]))
                print("_tiles[i+1:] " + str(_tiles[i+1:]))
                dfs(prefix+t, _tiles[:i] + _tiles[i+1:])
                print("_____________________________________")
        dfs('', tiles)
        return len(res) - 1 