import re

evaluations = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0
}

try:
    let_eval = input('Введіть оцінку(літеру):')
  
    if not re.match(r'^[ABCDF][\+\-]*$', let_eval):
        raise Exception('Не коректная оценка')

    num_eval = evaluations.get(let_eval[0])
    if len(let_eval) > 1:
        if let_eval[1] == '+':
            num_eval += 0.3
        else:
            num_eval -= 0.3

    print(num_eval)
except Exception as e:
    print(e)