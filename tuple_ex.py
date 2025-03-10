# Кортеж (tuple) — это упорядоченная, неизменяемая (immutable) коллекция в Python, 
# которая может содержать элементы разных типов.
# Основное отличие кортежа (tuple) от списка (list) в Python заключается в том, что списки 
# являются изменяемыми, а кортежи — нет.

# Это означает, что список можно изменить после его создания, добавив, удалив или изменив 
# один или несколько его элементов. В то время как кортежи являются неизменяемыми, то есть 
# после создания кортежа его нельзя изменить. Попытка сделать это приведёт к ошибке.

# Кроме того, кортежи занимают меньше памяти, чем списки, так как они неизменяемы.

# Выбор между использованием списка или кортежа зависит от конкретной задачи. Если известно,
# что данные не будут изменяться, или если важна экономия памяти, то лучше использовать 
# кортеж. Если же данные могут изменяться, то лучше выбрать список.
t1 = (1, 2, 3)  
t2 = ("apple", "banana", "cherry")  
t3 = (True, False, True)  