choco_bars = 18
people = 5
whole_bars = choco_bars // people
extra_bars = choco_bars % 7
left_over =  whole_bars * 7 % people
print("Whole chocolate bars each: {}".format(whole_bars))
print("Extra squares each: {}".format(extra_bars))
print("Left over squares: {}".format(left_over))
