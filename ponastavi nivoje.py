import json

with open("UVP\\Projektna-naloga\\nivoji.json", "w", encoding="utf-8") as f:
    json.dump({"1": [[[["", "", "", "", ""], ["-d", "w", "!", "", "!"], ["-w", "a", "", "", ""], ["", "!", "-s", "!", "-w"], ["", "", "", "", ""]], (0, 3), [(0, 2), (1, 2)]], float("inf")], "2": [[[["", "", ""], ["", "a", ""], ["", "", "-w"]], (0, 0), [(2, 2), (1, 1)]], float("inf")]}, f, indent=4)
    
