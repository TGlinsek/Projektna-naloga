import json

with open("UVP\\Projektna-naloga\\nivoji.json", "w", encoding="utf-8") as f:
    # json.dump({"1": [[[["", "", "", "", ""], ["-d", "w", "!", "", "!"], ["-w", "a", "", "", ""], ["", "!", "-s", "!", "-w"], ["", "", "", "", ""]], (0, 3), [(0, 2), (1, 2)]], float("inf")], "2": [[[["", "", ""], ["", "a", ""], ["", "", "-w"]], (0, 0), [(2, 2), (1, 1)]], float("inf")]}, f, indent=4)
    json.dump({'1': [[[['', '', ''], ['w', '', '-a'], ['', '', '']], [1, 1], [[0, 1], [2, 1]]], float("inf")], '2': [[[['', '', ''], ['-w', '', 'a'], ['', '', '']], [1, 1], [[2, 1], [0, 1]]], float("inf")], '3': [[[['', '', '-a'], ['', '-w', ''], ['w', '', '']], [0, 0], [[0, 2], [1, 1]]], float("inf")], '4': [[[['', '-s', ''], ['d', '', '-s'], ['', '-w', '']], [1, 1], 
[[0, 1], [2, 1]]], float("inf")], '5': [[[['', '', '', '-s'], ['', '!', 'd', ''], ['', 'a', '!', ''], ['-w', '', '', '']], [2, 0], [[2, 1], [3, 0]]], float("inf")], '6': [[[['', '-s', '', ''], ['', 'a', 'w', '-a'], ['-s', 'w', 'd', ''], ['', '', '-w', '']], [3, 0], [[1, 1], [0, 2]]], float("inf")], '7': [[[['', '', '', ''], ['-d', 'w', '', '-a'], ['-d', '', 'w', '-a'], ['-d', 'w', '', '-a']], [2, 0], [[1, 3], [0, 1]]], float("inf")], '8': [[[['', '-a', '-s', ''], ['-s', '', 'a', 'w'], ['d', 'w', '-w', '-a'], ['', '-w', 'w', '']], [1, 1], [[0, 2], [2, 0]]], float("inf")], '9': [[[['s', '', '-d', '', '!'], ['', '!', '', '', ''], ['', '', '', '!', ''], ['', '', '!', '-d', ''], ['', '!', '', '', '-a']], [0, 4], [[0, 0], [3, 3]]], float("inf")], '10': [[[['', '', '', '', ''], ['-d', 'w', '!', '', '!'], ['-w', 'a', '', '', ''], ['', '!', '-s', '!', '-w'], ['', '', '', '', 
'']], [0, 3], [[0, 2], [1, 2]]], float("inf")], '11': [[[['', '', '', '', 's'], ['-d', 'w', '-w', 'w', ''], ['', '!', '!', '!', ''], ['', 's', '-s', 's', '-a'], ['w', '', '', '', '']], [4, 2], [[4, 0], [4, 3]]], float("inf")], '12': [[[['', '', '', 's', ''], ['', '!', 'w', '', 'w'], ['-d', '', '', '!', ''], ['', '-a', '!', '', '-s'], ['-d', '', '', '-w', '']], [4, 4], [[4, 1], [3, 4]]], float("inf")], '13': [[[['', '', '-d', ''], ['', 'w', 'w', '']], [3, 1], [[2, 1], [2, 0]]], float("inf")], '14': [[[['', '', '', '-s', ''], ['', '-w', '-a', '', 'w']], [3, 1], [[4, 1], [1, 1]]], float("inf")], '15': [[[['', '', 'a', '', '', ''], ['', '', '-w', 'a', '-w', '']], [1, 0], [[3, 1], [2, 1]]], float("inf")], '16': [[[['', '', 'd', '-d', '', ''], ['-w', 'd', '', '', '', '-w']], [4, 1], [[2, 0], [5, 1]]], float("inf")], '17': [[[['d', '', '', '', '', ''], ['-w', '', 'd', '-w', '', '']], [4, 0], [[2, 1], [3, 1]]], float("inf")], 'Ogrevanje': [[[['', '', ''], ['w', '', '-a'], ['-d', '', '--w']], [1, 0], [[0, 1], [0, 2], [2, 2]]], float("inf")], 'Past 1': [[[['', '', 
'', '-s'], ['-w', '', 'a', ''], ['!', '-s', 'd', 's'], ['', '', '', '']], [0, 3], [[2, 2], [3, 0]]], float("inf")], 'Past 2': [[[['', '', '', '!', '!'], ['-w', '', 'a', '', '--a'], ['!', '-s', 'd', 's', '!'], ['', '', '', '', '!']], [0, 3], [[2, 2], [0, 1], [4, 1]]], float("inf")], 'Vogal': [[[['!', '', '--s', '', ''], ['!', '-d', '', 'd', ''], ['!', '--d', '-w', '!', '!'], ['--d', '', '', '!', '!']], [2, 1], [[3, 1], [1, 1], [0, 3]]], float("inf")], 'Vogal - obrat': [[[['!', '', '--s', '', ''], ['!', 'd', '', '-d', ''], ['!', '--d', '-w', '!', '!'], ['--d', '', '', '!', '!']], [2, 1], [[1, 1], [3, 1], [0, 3]]], float("inf")], 'Obhod': [[[['!', '!', '', '', '', '', '--a'], ['!', '', '', '!', '-s', '--a', '!'], ['!', '', '!', '!', '', 'a', '!'], ['', '', '', '', '--w', '', '!'], ['', '-a', '', '!', '!', '!', '!']], [4, 2], [[5, 2], [1, 4], [6, 0]]], float("inf")]}, f, indent=4)

"""
with open("UVP\\Projektna-naloga\\nivoji.json", "r", encoding="utf-8") as f: 
    a = json.load(f)
    print(a)  # to spravi v lepo obliko, le da morš inf zamenjat v float("inf")
"""
