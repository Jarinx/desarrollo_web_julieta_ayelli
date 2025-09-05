// Regiones y comunas de Chile

const regiones = [
    { id: 'rm', nombre: 'Región Metropolitana', comunas: ['Santiago', 'Maipú', 'Las Condes'] },
    { id: 'valp', nombre: 'Región de Valparaíso', comunas: ['Valparaíso', 'Viña del Mar', 'Quilpué'] },
    // Agregar más regiones y comunas según sea necesario
];


function getRegiones() {
    return regiones.map(region => ({ id: region.id, nombre: region.nombre }));
}
function getComunas(regionId) {
    const region = regiones.find(r => r.id === regionId);
    return region ? region.comunas : [];
}