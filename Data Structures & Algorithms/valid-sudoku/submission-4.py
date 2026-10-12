class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_sqrs = defaultdict(set)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                # skip empty
                if val == ".":
                    continue

                # check row
                if val in seen_rows[i]:
                    return False

                # check column
                if val in seen_cols[j]:
                    return False

                # check sqr
                if val in seen_sqrs[(i // 3,j // 3)]:
                    return False

                seen_rows[i].add(val)
                seen_cols[j].add(val)
                seen_sqrs[(i // 3,j // 3)].add(val)

        return True
