Example output of the P1-parser.awk:

```
$ lynx --dump http://192.168.1.1/P1/P1.txt | awk -f P1-parser.awk 
Electra: Totaal verbruik tarief 1 (nacht) KWh: 2015.82
Electra: Totaal verbruik tarief 2 (dag) KWh: 1756.94
Electra: Totaal geleverd tarief 1 (nacht) KWh: 354.852
Electra: Totaal geleverd tarief 2 (dag) KWh: 946.332
Electra: Huidig verbruik [W]: 0
Electra: Huidige teruglevering [W]: 30
Gas: Totaal verbruik gas in m3: 1463.19
```
