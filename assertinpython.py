# function to calculate percentage, given a list of marks out of 100
def percentage(marks):
  for m in marks:
    # marks should always be a positive value
    assert m > 0, "Only positive values allowed"
  return (sum(marks)/len(marks))
  
print(percentage([90,93,99,95,-94]))
