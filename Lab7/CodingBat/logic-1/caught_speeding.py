def caught_speeding(speed, is_birthday):
  increment = 5 if is_birthday else 0
    
  if speed <= 60 + increment:
    return 0
              
  if speed > 60 + increment and speed <= 80 + increment:
    return 1
                        
  return 2