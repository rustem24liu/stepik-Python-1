s = 'aTGcc' 
p = 'cc'

"""

- s.upper() -> 'ATGCC'
- s.lower -> 'atgcc'
- s.count(p) -> 1(because p = cc and cc in s is one,as you can see the last letters)
- s.find(p)-> 3 {первое вхождение (индекс) p in c}
- s.find("A") -> -1 {строка 'A' не входит в s, так как он не нашел букву 'А' он вывел -1}
- s.replace('c', 'C') -> 'aTGCC' {поменяем все вхождение с на С}

"""