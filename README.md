# Germany Holidays

This repository contains a small script, which downloads and parses 
the public holidays of the german federal states (Augsburg city holidays are not
included). The results are written
to JSON files in the results folder. The holidays (and their names) are downloaded from 
https://www.ferienkalender.com/ and other years than the included one are only available,
if the respective website provides them. <br/>
THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY!

### Install
```console
foo@bar:~$ pip install -r requirements.txt
```

### Run - without names
```console
foo@bar:~$ python3 main.py
```

### Run - with names
```console
foo@bar:~$ python3 main.py true
```

### Results - without names
```json
{
  "Baden-Wuerttemberg": [
    "01.01.2022",
    "06.01.2022",
    "15.04.2022",
    "18.04.2022",
    "01.05.2022",
    "26.05.2022",
    "06.06.2022",
    "16.06.2022",
    "03.10.2022",
    "01.11.2022",
    "25.12.2022",
    "26.12.2022"
  ],
  "Bayern": [
    ...
  ],
  ...
}
```

### Results - with names
```json
{
  "Baden-Wuerttemberg": [
    {
      "holiday": "Neujahr",
      "date": "01.01.2022"
    },
    {
      "holiday": "Heilige Drei K\u00f6nige",
      "date": "06.01.2022"
    },
    {
      "holiday": "Karfreitag",
      "date": "15.04.2022"
    },
    {
      "holiday": "Ostermontag",
      "date": "18.04.2022"
    },
    {
      "holiday": "Tag der Arbeit",
      "date": "01.05.2022"
    },
    {
      "holiday": "Christi Himmelfahrt",
      "date": "26.05.2022"
    },
    {
      "holiday": "Pfingstmontag",
      "date": "06.06.2022"
    },
    {
      "holiday": "Fronleichnam",
      "date": "16.06.2022"
    },
    {
      "holiday": "Tag der Deutschen Einheit",
      "date": "03.10.2022"
    },
    {
      "holiday": "Allerheiligen",
      "date": "01.11.2022"
    },
    {
      "holiday": "1. Weihnachtsfeiertag",
      "date": "25.12.2022"
    },
    {
      "holiday": "2. Weihnachtsfeiertag",
      "date": "26.12.2022"
    }
  ],
  "Bayern": [
    ...
  ],
  ...
}
```
