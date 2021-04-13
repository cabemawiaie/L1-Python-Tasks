choco_bars = 18
people = 5
whole_bars = choco_bars // people
extra_bars = choco_bars % 7
left_over =  whole_bars * 7 % people
print("Whole chocolate bars each: {} \n Extra squares each: {} \n Left over squares: {}".format(whole_bars, extra_bars, left_over))
