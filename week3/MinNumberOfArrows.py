class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0 or len(points[0]) == 0:  # Handles cases where there are no baloons.
            return 0
        points.sort()  # sorts the list based on start coordinate
        arrows = 1  # arrows counter
        start = points[0][0]  # interval start tracking pointer
        end = points[0][1]  # interval end tracking pointer
        for i in range(1, len(points)):  # looping through all balloons
            if points[i][
                0] <= end:  # if current ballon has common interval with previous interval, same arrow will pass through it,
                # no need to add extra arrow
                start = max(start, points[i][0])  # modifies interval with new bounds
                end = min(end, points[i][1])
            else:  # if current balloon out of previous interval, a new arrow is required.
                arrows += 1
                start = points[i][0]  # modifies interval with new bounds
                end = points[i][1]
        return arrows
