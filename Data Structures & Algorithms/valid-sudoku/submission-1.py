class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(set)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                # skip empty
                if val == ".":
                    continue

                # check row
                if val in (seen_row := seen[f"row::{i}"]):
                    return False

                seen_row.add(val)

                # check column
                if val in (seen_col := seen[f"col::{j}"]):
                    return False

                seen_col.add(val)

                # check sqr
                if val in (seen_sqr := seen[f"sqr::[{i // 3},{j // 3}]"]):
                    return False

                seen_sqr.add(val)

        return True
