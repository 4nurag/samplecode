def clamp_number(num,a,b):
  return max(min(num, max(a, b)), min(a, b))

clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
