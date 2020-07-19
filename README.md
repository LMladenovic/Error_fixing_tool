## C program auto fix tool using Valgrind to detect bugs

### Opis projekta

Alat koji automatski otkriva greske u kodu napisanom u C-u koristeci alat Valgrind, a zatim ih ispravlja ukoliko je to u njegovoj moci. Razvijan pod Linux okruzenjem. Alat je nazvan Koronka, zbog trenutne situacije u kojoj se svi nalazimo. Osnovna svrha alata je demonstracija rada alata Valgrind, kao i tumacenje izvestaja o greskama koje Valgrind daje i njihovo uspesno otklanjanje.

### Podesavanje okruzenja

Pre upotrebe alata potrebno je instalirati:
- [GCC kompajler](https://linuxize.com/post/how-to-install-gcc-compiler-on-ubuntu-18-04/)
- [Valgrind alat](https://wiki.ubuntu.com/Valgrind)
- [Python](https://docs.python-guide.org/starting/install3/linux/)

### Upotreba alata

Pokrenuti komangu 
<pre> git clone https://github.com/LMladenovic/FixMe.git </pre>

Pozicionirati se u folderu gde se nalazi glavni fajl <i>koronka.py</i>, kao i pomocni fajlovi u okviru foldera <i>utils</i>.

Alat se pokrece komandom
<pre> python koronka.py [c file|path to c file] [other arguments] </pre>

Alat ce u okviru direktorijuma u kom se nalazi kreirati folder po modelu datumPokretanja-VremePokretanja, u njega kopirati gore navedeni fajl kao argument nad kojim ce vrsiti ispravku, njih menjati, i na kraju generisati ExecutionReport sa izvestajem sta je i na koji nacin promenjeno. Na taj nacin originalni fajl ostaje nepromenjen, a rezultat rada alata i izmenjeni fajl se nalazi u pomenutom folderu. 

### Studenti koji rade na projektu

- [Lazar Mladenovic](https://github.com/LMladenovic)
- [Tatjana Radovanovic](https://github.com/Tatjana95)
- [Jovan Maric](https://github.com/maric993)
