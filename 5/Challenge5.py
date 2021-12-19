def parseInputToMatrix():
  result = []
  with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.split('\n')

    for line in lines:
      result.append([int(char) for char in line])

  return result

def getCommonValueInColumn(matrix, col):
  column = []
  for row in range(len(matrix)):
    column.append(matrix[row][col])

  return max(set(column), key = column.count)

def invertArray(array):
  result = []
  for item in array:
    result.append(1-item)
  return result

def parseToDecimal(array):
  string_ints = [str(int) for int in array]
  return int(''.join(string_ints), 2)


def main():
    matrix = parseInputToMatrix()
    
    mostCommonValues = []
    for col in range (len(matrix[0])):
      mostCommonValues.append(getCommonValueInColumn(matrix, col))      

    leastCommonValues = invertArray(mostCommonValues)

    gamma  = parseToDecimal(mostCommonValues)  
    epsilon= parseToDecimal(leastCommonValues)  
    
    print(gamma* epsilon)

main()