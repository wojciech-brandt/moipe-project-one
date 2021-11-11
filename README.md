# 1. Wstęp
Każdy student otrzyma dwa indywidualne problemy do rozwiązania w trakcie zajęć projektowych. Pierwszy z projektów dotyczy analizy układu jednowymiarowego. Układ posiada jedno
wejście i jedno wyjście.
Zachowanie analizowanego obiektu odtwarza plik wykonywalny o nazwie **zXXvXX.exe** (wirtualny pomiar). Program przyjmuje wyłącznie argumenty numeryczne z kropką dziesiętną. Zatem
wywołanie programu powinno wyglądać następująco: zXXvXX.exe a1, gdzie argument a1 to,
na przykład, wartość **12.34**.

# 2. Cele projektu
Student:
 oswoi się ze sposobem badania układów przed następnym projektem,
 zapozna się z metodami opracowywania zależności empirycznych i badania ich zgodności.

# 3. Zakres
Do rozwiązania problemów związanych z realizacją projektu można wykorzystać inżynierskie
pakiety np.:
 Matlab,
 Octave,
 Python z biblioteką PyDOE2, numpy,
 środowisko R.
 własny program w dowolnym języku programowania.
W trakcie realizacji pierwszego zadania projektowego należy zrealizować kroki opisane w
poniższych podrozdziałach.

## 3.1. Badanie wstępne
Zadaniem badań wstępnych jest pozyskanie ogólnej wiedzy na temat zachowania układu.
Należy wyznaczyć następujące wielkości:
 wartość parametru wyjściowego na granicach przedziału,
 wartości ekstremów lokalnych (jeżeli istnieją),
 zakres zmian parametru wyjściowego w rozpatrywanym przedziale,
 parametry statystyczne (bez wykorzystania gotowych funkcji) dla wybranego punktu pomiarowego tj.:
— wielkość próby (liczba powtórzeń dla jednego wybranego punktu pomiarowego co najmniej 25),
— średnia,
— mediana,
— wariancja,
— odchylenie standardowe,
— minimum,
— maksimum,
— histogram.
W badaniach wstępnych należy też przyjrzeć się charakterystyce układu w różnych skalach:
liniowej i logarytmicznej. W ten sposób można wykryć podstawowe charakterystyczne zależności.
## 3.2. Eksperyment właściwy
W ramach eksperymentu właściwego należny wykonać następujące zadania:
1. Dla zadanego zakresu zmiennych wejściowych dokonać ich standaryzacji (przeskalowania do
przedziału [−1, 1]. W eksperymencie właściwym nie należy wybierać więcej niż 20
punktów pomiarowych.
2. Opracować model obiektu badań. Zaproponować trzy do pięciu modeli z różnymi funkcjami bazowymi. Można też użyć funkcji wymiernych, wykładniczych lub logarytmicznych. W
każdym modelu wyznaczyć wartości współczynników najlepiej metodą najmniejszych kwadratów. Współczynniki wyznaczyć dla każdego modelu we współrzędnych naturalnych oraz
we współrzędnych standaryzowanych. Należy podać otrzymane układy równań normalnych.
3. Ocenić adekwatność przyjętych modeli. Zgodność modelu można ocenić wizualnie (wykres).
Oprócz wizualnej oceny zgodności uzyskanych przebiegów należy wyznaczyć:
 współczynnik determinacji (R2
),
 pierwiastek błędu średnio kwadratowego (RSME),
 średni oraz maksymalny błąd względny,
 średni oraz maksymalny błąd bezwzględny.
4. Wybrać model najlepiej opisujący badany obiekt. Ocenić odchyłki dopasowania w badanym
zakresie.
## 3.3. Wnioski
We wnioskach należy odnieść się do tego na ile warto stosować wybrane modele do badanego
obiektu oraz zaproponować postępowanie, które może zapewnić lepsze odwzorowanie obiektu.
2
# 4. Forma sprawozdania
Sprawozdanie z realizacji projektu należy sporządzić w postaci elektronicznej. Plik w formacie
pdf ma zawierać opis realizacji poszczególnych kroków dokumentując przebieg projektu. Jednym
z kryteriów oceny jest estetyka przygotowanego sprawozdania, z tego powodu nie należy tej części
zadania odkładać na ostatnią chwilę. Zazwyczaj bardzo pozytywnie na estetykę dokumentu przy
jednoczesnym małym nakładzie pracy wpływa przygotowanie go za pomocą systemu składu
tekstu TEX z makrami LATEX. Można wykorzystać klasę mwart.
