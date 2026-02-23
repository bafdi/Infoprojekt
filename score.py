def get_new_score(player_path, point_locations):
    path_lines = []
    gathered_points = 0

    for i in range(0, len(player_path) - 1):
        pos_1 = player_path[i]
        pos_2 = player_path[i + 1]
        path_line = tuple(sorted((pos_1, pos_2)))
        path_lines.append(path_line)


    for point in point_locations:
        if point in path_lines:
            gathered_points += 1

    return gathered_points