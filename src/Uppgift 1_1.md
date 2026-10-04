### A
Matchar ord som innehåller bokstavssekvensen ab som i sabotör.

### B
Case insensitive /i

### C
Bokstaven a kan förekomma noll eller flera gånger före ett n. Strängar som matchar är tex n, an, aan och aaan.

### D
a eller e följd av n. inconsequential matchar

### E
Börjar på "je", ".+" en eller flera valfria tecken följt av ett e.
"jeppe och je je" matchar.

### F
Matchar ett blanksteg följt av a, eventuellt ett n, och sedan ett blanksteg. C och D matchar.

### E
A: Matchar strängar som innehåller "line" eller "lines". s är valfri eftersom ? betyder 0 eller 1 gång.

B: Matchar strängar som börjar med 0 eller flera a och slutar med ett ö. Det får inte finnas några andra tecken i strängen

C: [aeiouyåäö]+ En av detta tecken i hakparenteserna och + innebär en eller flera gånger.

D: Första siffran måste vara 1-9 och därefter kan det vara 0 eller fler siffror.

E: \d{4} = exakt 4 siffror, \d{4}-\d{2}-\d{2} = yyyy-mm-dd
