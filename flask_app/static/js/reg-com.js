// Regiones y comunas de Chile

const regiones = [
  { id: "arica", nombre: "Arica y Parinacota", comunas: ["Arica","Camarones","Putre","General Lagos"] },
  { id: "tarapaca", nombre: "Tarapacá", comunas: ["Iquique","Alto Hospicio","Pozo Almonte","Pica","Camiña","Huara","Colchane"] },
  { id: "antofagasta", nombre: "Antofagasta", comunas: ["Antofagasta","Mejillones","Sierra Gorda","Taltal","Calama","Ollagüe","San Pedro de Atacama"] },
  { id: "atacama", nombre: "Atacama", comunas: ["Copiapó","Caldera","Tierra Amarilla","Vallenar","Freirina","Huasco","Diego de Almagro","Chañaral","Alto del Carmen"] },
  { id: "coquimbo", nombre: "Coquimbo", comunas: ["La Serena","Coquimbo","Andacollo","La Higuera","Paihuano","Vicuña","Illapel","Los Vilos","Salamanca","Ovalle","Combarbalá","Monte Patria","Punitaqui","Río Hurtado"] },
  { id: "valparaiso", nombre: "Valparaíso", comunas: ["Valparaíso","Viña del Mar","Concón","Quilpué","Villa Alemana","Casablanca","Quintero","Puchuncaví","Quillota","La Calera","La Cruz","Nogales","San Antonio","Cartagena","El Quisco","El Tabo","Santo Domingo","San Felipe","Llaillay","Putaendo","Catemu","Santa María","Los Andes","Calle Larga","Rinconada","San Esteban","Isla de Pascua","Juan Fernández"] },
  { id: "rm", nombre: "Región Metropolitana de Santiago", comunas: [
      "Santiago","Cerrillos","Cerro Navia","Conchalí","El Bosque","Estación Central","Huechuraba","Independencia","La Cisterna","La Florida","La Granja","La Pintana","La Reina","Las Condes","Lo Barnechea","Lo Espejo","Lo Prado","Macul","Maipú","Ñuñoa","Pedro Aguirre Cerda","Peñalolén","Providencia","Pudahuel","Quilicura","Quinta Normal","Recoleta","Renca","San Joaquín","San Miguel","San Ramón","Vitacura",
      "Puente Alto","Pirque","San José de Maipo","Colina","Lampa","Tiltil","San Bernardo","Buin","Calera de Tango","Paine","Melipilla","Alhué","Curacaví","María Pinto","San Pedro","Talagante","El Monte","Isla de Maipo","Padre Hurtado","Peñaflor"
    ] },
  { id: "ohiggins", nombre: "Libertador General Bernardo O'Higgins", comunas: ["Rancagua","Machalí","Graneros","Mostazal","Codegua","Doñihue","Coltauco","Olivar","Requínoa","Rengo","Malloa","San Vicente","Peumo","Pichidegua","Las Cabras","San Fernando","Chimbarongo","Nancagua","Placilla","Santa Cruz","Lolol","Paredones","Pichilemu","Navidad","Litueche","La Estrella","Marchigüe"] },
  { id: "maule", nombre: "Maule", comunas: ["Talca","Maule","San Clemente","Pelarco","Pencahue","Río Claro","Curepto","Constitución","San Javier","Villa Alegre","Yerbas Buenas","Linares","Colbún","Longaví","Parral","Retiro","Cauquenes","Chanco","Pelluhue"] },
  { id: "nuble", nombre: "Ñuble", comunas: ["Chillán","Chillán Viejo","Quillón","Bulnes","San Ignacio","Pinto","Coihueco","El Carmen","Pemuco","Yungay","San Carlos","Ñiquén","San Fabián","Coelemu","Ránquil","Portezuelo","Treguaco","Cobquecura","Quirihue","Ninhue"] },
  { id: "biobio", nombre: "Biobío", comunas: ["Concepción","Talcahuano","Hualpén","Chiguayante","San Pedro de la Paz","Penco","Tomé","Coronel","Lota","Florida","Hualqui","Santa Juana","Los Ángeles","Nacimiento","Laja","San Rosendo","Yumbel","Cabrero","Mulchén","Quilaco","Quilleco","Santa Bárbara","Tucapel","Antuco","Arauco","Cañete","Contulmo","Curanilahue","Lebu","Los Álamos","Tirúa"] },
  { id: "araucania", nombre: "La Araucanía", comunas: ["Temuco","Padre Las Casas","Cunco","Melipeuco","Curarrehue","Pucón","Villarrica","Gorbea","Lautaro","Perquenco","Galvarino","Cholchol","Carahue","Nueva Imperial","Saavedra","Teodoro Schmidt","Toltén","Loncoche","Pitrufquén","Freire"] },
  { id: "los-rios", nombre: "Los Ríos", comunas: ["Valdivia","Máfil","Mariquina","Lanco","Los Lagos","Panguipulli","Corral","Paillaco","La Unión","Río Bueno","Futrono","Lago Ranco"] },
  { id: "los-lagos", nombre: "Los Lagos", comunas: ["Puerto Montt","Puerto Varas","Llanquihue","Frutillar","Cochamó","Calbuco","Maullín","Los Muermos","Osorno","Río Negro","Purranque","San Pablo","Puerto Octay","Puqueldón","Queilén","Quellón","Quinchao","Ancud","Castro","Dalcahue","Chonchi","Curaco de Vélez"] },
  { id: "aysen", nombre: "Aysén del General Carlos Ibáñez del Campo", comunas: ["Coyhaique","Aysén","Cisnes","Guaitecas","Lago Verde","Chile Chico","Río Ibáñez","Tortel","O'Higgins","Cochrane"] },
  { id: "magallanes", nombre: "Magallanes y de la Antártica Chilena", comunas: ["Punta Arenas","Puerto Natales","Torres del Paine","Porvenir","Primavera","Timaukel","Cabo de Hornos","Antártica"] }
];


function getRegiones() {
    return regiones.map(region => ({ id: region.id, nombre: region.nombre }));
}
function getComunas(regionId) {
    const region = regiones.find(r => r.id === regionId);
    return region ? region.comunas : [];
}