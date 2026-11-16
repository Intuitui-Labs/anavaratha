# Waste types → household route status (sankey)

```mermaid
sankey-beta

"Household & commercial MSW","HH route: yes",1
"Household & commercial MSW","HH route: conditional",1
"Plastics","HH route: yes",2
"Plastics","HH route: conditional",2
"Paper & cardboard","HH route: yes",2
"Paper & cardboard","HH route: conditional",1
"Metal scrap","HH route: yes",1
"Metal scrap","HH route: conditional",2
"Glass","HH route: conditional",1
"Glass","HH route: yes",1
"Textiles & clothes","HH route: yes",3
"Textiles & clothes","HH route: conditional",2
"Textiles & clothes","HH route: no route found",1
"Textiles & clothes","HH route: no",1
"Organics & agriculture","HH route: conditional",2
"Organics & agriculture","HH route: yes",1
"Organics & agriculture","HH route: no route found",3
"E-waste, batteries, appliances, toner","HH route: yes",5
"E-waste, batteries, appliances, toner","HH route: no route found",2
"Household hazardous & clinical","HH route: no route found",6
"Household hazardous & clinical","HH route: no",1
"Tyres, vehicles, ship-breaking","HH route: no route found",3
"Tyres, vehicles, ship-breaking","HH route: no",1
"Tyres, vehicles, ship-breaking","HH route: yes",1
"Construction & bulky","HH route: no",1
"Construction & bulky","HH route: no route found",2
"Construction & bulky","HH route: conditional",1
"Construction & bulky","HH route: not found",1
"Industrial hazardous & oils","HH route: no",5
"Industrial hazardous & oils","HH route: yes",1
"Marine & fishing","HH route: no",2
"Marine & fishing","HH route: no route found",1
"Energy & sanitation","HH route: no route found",2
```

![render](g_route_sankey.png)

**Sources:** `neevsk-research/anavaratha/phase1/WASTE_TAXONOMY_LK.md` type tables, "HH route" column (62 types).

**Notes:** Unit = number of waste **types**, not tonnage. Uses `sankey-beta`. Checked 2026-11-16: GitHub renders it natively, so no swap was needed. The PNG stays for viewers without Mermaid.
