#ГЕНЕРАТОР БЕЗОПАСНЫХ ПАРОЛЕЙ
from random import*
digits = "0123456789"
password = []
chars = ''
lo = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = "!#$%&*+-=?@^"
def dobavka(chtoto):
 d_n = input()
 if d_n == "да" or d_n == "Да":
  for i in range(len(chtoto)):
   password.append(chtoto[i])
print('Включать ли цифры в пароль?')
dobavka(digits)
print('Включать ли заглавные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ" в пароль?')
dobavka(u)
print('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz" в пароль?')
dobavka(lo)
print('Включать ли символы "!#$%&*+-=?@^" в пароль?')
dobavka(p)
print("Исключать ли неоднозначные символы 'il1Lo0O'?")
otv = input()
if otv == "да" or otv == "Да":
 s = "il1Lo0O"
 for v in range(len(s)):
  if s[v] in password:
   password.remove(s[v])
print('Из скольки символов сгенерировать пароль?')
kolichestvo = int(input())
f = sample(password, kolichestvo)
if kolichestvo > len(f):
 print("Недостаточно допустимых символов, чтобы создать пароль")
for m in range(len(f)):
 chars = chars + f[m]
print(chars)
