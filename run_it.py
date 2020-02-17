from ceasar_exercise.encrypt import encrypt as e
from ceasar_exercise.decrypt import decrypt as d
my_plain_text=e("o l i v e r",7)
print(my_plain_text)
my_ceasar=d(my_plain_text,7)
print(my_ceasar)