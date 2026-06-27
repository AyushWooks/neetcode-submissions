class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:

            if matrix[top][-1] < target:
                top += 1

            elif matrix[top][0] > target:
                return False

            else:
                l = 0
                r = len(matrix[top]) - 1

                while l <= r:
                    mid = (l + r) // 2

                    if matrix[top][mid] < target:
                        l = mid + 1
                    elif matrix[top][mid] > target:
                        r = mid - 1
                    else:
                        return True

                return False

        return False