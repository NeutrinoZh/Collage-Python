# 1 (0,3)
import re
print((lambda text: re.sub(r'[aeyuio]', '', text))(input('text:')))