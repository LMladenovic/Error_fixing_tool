## C program auto fix tool using Valgrind to detect bugs

### Opis projekta

Alat koji automatski otkriva greske u kodu napisanom u C-u koristeci alat Valgrind, a zatim ih ispravlja ukoliko je to u njegovoj moci. Razvijan pod Linux okruzenjem. Alat je nazvan Koronka, jer je razvijan u vreme pandemije Korona virusa, a sa ciljem da bar nesto dobro nastane sa pomenutim imenom. Osnovna svrha alata je demonstracija rada alata Valgrind, kao i automatsko tumacenje izvestaja o greskama koje Valgrind daje i njihovo uspesno otklanjanje.


[Link do projekta](https://github.com/MATF-Software-Verification/05_error_fixing_tool.git) u okviru MATF Software verification organizacije po cijoj je ideji nastavljen razvoj i nastao alat kakav danas i jeste. 
 
### Podesavanje okruzenja

Pre upotrebe alata potrebno je instalirati:
- [GCC kompajler](https://linuxize.com/post/how-to-install-gcc-compiler-on-ubuntu-18-04/)
- [Valgrind alat](https://wiki.ubuntu.com/Valgrind)
- [Python](https://docs.python-guide.org/starting/install3/linux/)

### Upotreba alata

Pokrenuti komandu 
<pre> git clone https://github.com/LMladenovic/Error_fixing_tool.git </pre>

Pozicionirati se u direktorijum u kom se nalazi glavni fajl <i>koronka.py</i>, kao i pomocni fajlovi u okviru direktorijuma <i>utils</i>.

Alat se pokrece komandom
<pre> python3 koronka.py [files=[list of files]] [structures=[list of user defined structures]] [path to c file] [other arguments] </pre>

[other arguments] - argumenti koji su potrebni C programu kao argumenti komandne linije ( u trenutnoj verziji projekta)  
[files = [list of files]] - dodatni fajlovi potrebni programu (npr. .h fajlovi)  
[structures=[list of user defined structures]] - korisnicki definisane strukture (npr. Cvor stabla)  

Alat ce u okviru direktorijuma u kom se nalazi kreirati direktorijum po modelu datumPokretanja-VremePokretanja i u njega kopirati gore navedeni fajl kao argument nad kojim ce vrsiti ispravku, kao i fajlove navedene u okviru argumenta files. Nad njima ce alat vrsiti odgovarajuce promene u skladu sa pronadjenim greskama i njihovim ispravkama, i na kraju generisati ExecutionReport sa izvestajem sta je i na koji nacin promenjeno. Na taj nacin originalni fajlovi ostaju nepromenjeni, a rezultat rada alata i izmenjeni fajlovi se nalaze u pomenutom direktorijumu. 
