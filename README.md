# InheritanceOfClasses
**Задача:** промоделировать процесс множественного наследования классов, и понять существует ли путь от одного класса до другого. Hеобходимо отвечать на запросы, является ли один класс предком другого класса

**Формат входных данных**

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

**Формат выходных данных**

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:

4

A

B : A

C : A

D : B C

4

A B

B D

C D

D A

**Sample Output:**

Yes

Yes

Yes

No

