# [OverPass Turbo](https://overpass-turbo.eu)

## déterminer les tronçons autoroutiers limités à 90 km/h et des lampadaires autour de Toulouse
```
way
  [highway=motorway]
  [maxspeed=90]
  [lit=yes]
  ({{bbox}});
out geom;
```

## Trouver toutes les rues (highway) de Labège (31) limitées à 30 km/h
```
{{geocodeArea:Labège}}->.searchArea;
way [highway] [maxspeed=30]
  (area.searchArea);
out geom;
```

## Trouver tous les bars de Blagnac (31)
```
{{geocodeArea:Blagnac}}->.searchArea;
node [amenity="bar"](area.searchArea);
out geom;
```

## Chercher toutes les limites de communes autour de Toulouse
```
relation [boundary="administrative"][admin_level=8]
 ({{bbox}});
out body;
```

## Trouver toutes les forêts de la commune de Léguevin (31)
```
{{geocodeArea:”Léguevin”}}->.searchArea;

relation[landuse="forest"](area.searchArea);
out geom;
```

## Toutes les routes de Montlaur (31) qui ont une vitesse limite de plus 50 km/h
```
{{geocodeArea:"Montlaur"}}->.searchArea;
(
  way["highway"]
  (if: (is_number(t["maxspeed"]) && t["maxspeed"] > 50))(area.searchArea);
);
```

## Afficher le nombre de bâtiments recensés de Mervilla (31) suivant leur type 
```
[out:csv(::count, ::"count:nodes", ::"count:ways", ::"count:relations")][timeout:25];
{{geocodeArea:"Mervilla"}}->.searchArea;
(
  node["building"="yes"](area.searchArea);
  way["building"="yes"](area.searchArea);
  relation["building"="yes"](area.searchArea);
);

out count;
```

## Trouver les bars de Toulouse (31) à moins de 100 m d’une station de métro
```
[out:json][timeout:25];
area[name="Toulouse"];
node(area)["public_transport"="stop_position"] ["subway"="yes"] ;
node(around:100)[amenity=“bar”]
out body;
```

## Trouver les bâtiments isolés de Arvieux (05) à plus de 100 m d’une autre habitation
```
[out:json][timeout:30];

{{geocodeArea:"Arvieux"}}->.searchArea;

way[building](area.searchArea)->.isole;

foreach.isole (
	way.isole(around:100);
	way._(if:count(ways) == 1);
	out center;
);

out body;
```

## Trouver toutes les intersections entre des routes et des voies ferrées à Baziège (31)
```
[out:json][timeout:30];

{{geocodeArea:"Baziège"}}->.searchArea;

way["railway"="rail"](area.searchArea)->.major;
way["highway"](area.searchArea)->.minor;
node(w.major)(w.minor);

// print results
out body;
```

## Afficher toutes les écoles de Tournefeuille (31) en bleu
```
out:json][timeout:25];

{{geocodeArea:"Tournefeuille"}}->.searchArea;
(  
  {{style:
    node[building="school"]{color:blue; fill-color:blue;}
    way[building="school"]{color:blue; fill-color:blue;}
    relation[building="school"]{color:blue; fill-color:blue;}
  }}
  nwr[building="school"](area.searchArea);
);

(._;>;);
out body;

```

## Trouver les bars à Toulouse à moins de 100 m d’une station de métro (déjà fait) et afficher leur nom
```
[out:json][timeout:25];
area[name="Toulouse"];

{{style:
  node{ text: name;}
}}

node(area)["public_transport"="stop_position"] ["subway"="yes"] ;
node(around:100)[amenity="bar"];
out;
```

## Représenter tous les arrêts de bus de Castanet-Tolosan (31) et afficher leur nom 
```
[out:json][timeout:25];

{{geocodeArea:"Castanet-Tolosan"}}->.searchArea;
(  
  {{style:
	  node[highway=bus_stop] {
	    icon-image: url('icons/maki/bus-18.png');
	    icon-width: 18;}
    node{ text: name;}
	}}
  node[highway="bus_stop"](area.searchArea);
);
out body;
```






