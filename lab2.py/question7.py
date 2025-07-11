points_list = [(4, 8), (5, 10), (6, 12), (7, 14), (8, 16)]

if len(points_list) < 2:
    print("The points lie on a straight line.")
else:
    (x_first, y_first), (x_second, y_second) = points_list[0], points_list[1]
    diff_x = x_second - x_first
    diff_y = y_second - y_first

    for i in range(2, len(points_list)):
        x_curr, y_curr = points_list[i]
        if diff_y * (x_curr - x_first) != diff_x * (y_curr - y_first):
            print("The points are not collinear.")
            break
    else:
        print("The points lie on a straight line.")

