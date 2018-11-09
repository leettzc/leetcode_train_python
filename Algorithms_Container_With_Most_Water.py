height=[]
r_h = 0
last_height = len(height) - 1
first_height = 0
while last_height != first_height:
    if height[first_height] < height[last_height]:
        r_h = max(r_h, (last_height - first_height) * height[first_height])
        first_height += 1
    else:
        r_h = max(r_h, (last_height - first_height) * height[last_height])
        last_height -= 1
print(r_h)