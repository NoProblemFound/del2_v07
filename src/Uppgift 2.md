# 2
### 1a:
\d+\scm
- \d+ = En eller flera siffror
- \s = Ett mellanslag
- cm = Innehåller "cm" efter mellanslaget

### 1b
\d+\scm.*\d+\scm

\d+\scm hittar en längd i centimeter som i föregående övning. 
.* tillåter valfria tecken mellan längderna. 
Därefter används \d+\scm igen för att hitta en andra längd.

### 1c
\d+(,\d+)?\s(cm|m).*\d+(,\d+)?\s\2

- \d+ = en eller flera siffror
- (,\d+)? = Valfri antal decimaler
- \s = En mellanslag
- (cm|m) = Antingen cm eller m
- .* = Valfri antal tecken mellan längderna.

### 2
\d{3}\s\d{2}
- \d{3} = Exakt 3 siffror
- \s = ett mellanslag
- \d{2} = Exakt 2 siffror

### 3
\d{4}-\d{2}-\d{2}
- \d{4} = Exakt 4 siffror
- "-" = Ett bindestreck

### 4
\d+(,\d{2})?\s?kr
- \d+ = En eller flera siffror
- (,\d{2})? = Valfri med 2 decimaler
- \s = valfritt med ett mellanslag
- kr = avslutar med kr.

### 5a
[A-Za-z0-9.-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]
- [A-Za-z0-9.-]+ = en eller flera bokstäver, siffror, punkt eller bindestreck
- @ = snabel-a
- [A-Za-z0-9.-]+ = servernamnet
- \. = en punkt (måste escape:as eftersom . annars betyder vilket tecken som helst)
- [A-Za-z0-9]+ = domänen
