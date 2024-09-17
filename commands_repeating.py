def solution(commands):
    command_map = {"mv":0,"ls":0,"cp":0}
    command_set = list(command_map.keys())
    for command in commands:
        if command in command_set:
            command_map[command] += 1
        else:
            while command not in command_set:
                number = int(command.split('!')[1])
                command = commands[number-1]
            command_map[command] += 1
    return command_map

print(solution(["ls", "cp", "mv", "mv", "!1", "!5"]))

        