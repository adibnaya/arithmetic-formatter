def arithmetic_arranger(problems, result=False):
  """
    Receives a list of strings that are arithmetic problems and
    returns the problems arranged vertically and side-by-side. 
    
    If result is set to True, the answers will be displayed.

    Error handling:
        `Error: Too many problems.`: More than 5 problems were given.
        `Error: Operator must be '+' or '-'.`: The allowed operators are + and -. 
        `Error: Numbers must only contain digits.`: Each number should only contain digits.
        `Error: Numbers cannot be more than four digits.`: Each number has a max of four digits.

    This is an assignment of https://www.freecodecamp.org/ In this version I made sure to
    pass all the tests and requirements of the assignment and also added the option to have
    problems with more then 2 numbers.
  """
  max_problems = 5
  allowed_ops = ['+', '-']
  formatted_problems = []
  top = []
  bottom = []
  lines = []
  results = []

  if len(problems) > max_problems:
    return "Error: Too many problems."

  for problem in problems:
    chunks = problem.split()
    max_len = len(max(chunks, key=len))

    if not all([i.isnumeric() for i in chunks[::2]]):
      return "Error: Numbers must only contain digits."
    elif any([i not in allowed_ops for i in chunks[1::2]]):
      return "Error: Operator must be '+' or '-'."
    elif max_len > 4:
      return "Error: Numbers cannot be more than four digits."

    line_len = max_len + 2  # add 2 to align the operation display

    line = '-' * line_len
    first_num = chunks[0].rjust(line_len, ' ')
    second_num = ""
    for i in range(0, len(chunks[1::2])):
      if second_num == "":
        second_num = f"{chunks[1::2][i]}{' ' * (line_len - len(chunks[2::2][i]) - 1)}{chunks[2::2][i]}"
      else:
        second_num += f"\n{chunks[1::2][i]}{' ' * (line_len - len(chunks[2::2][i]) - 1)}{chunks[2::2][i]}"

    bottom.append(second_num)
    top.append(first_num)
    lines.append(line)

    if result:
      res = str(eval(problem))
      results.append(f"{res.rjust(line_len, ' ')}")

  formatted_problems = '\n'.join(
    ['    '.join(i) for i in (top, bottom, lines)])

  if results:
    formatted_problems += '\n' + '    '.join(results)

  return formatted_problems
