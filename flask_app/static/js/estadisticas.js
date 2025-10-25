(async function () {
  async function cargarDatos() {
    const resp = await fetch("/api/estadisticas");
    if (!resp.ok) {
      console.error("Error al cargar estadísticas");
      return null;
    }
    return resp.json();
  }

  function dibujarLinea(avisosPorDia) {
    const categorias = avisosPorDia.map(p => p.dia);
    const data = avisosPorDia.map(p => p.avisos);

    Highcharts.chart('chart-linea', {
      chart: { type: 'line' },
      title: { text: 'Avisos por día' },
      xAxis: { categories: categorias, title: { text: 'Día' } },
      yAxis: { title: { text: 'Cantidad de avisos' } },
      series: [{
        name: 'Avisos',
        data: data
      }],
      legend: { enabled: false }
    });
  }

  function dibujarTorta(totalPorTipo) {
    const data = totalPorTipo.map(item => ({
      name: item.tipo,
      y: item.total
    }));

    Highcharts.chart('chart-torta', {
      chart: { type: 'pie' },
      title: { text: 'Avisos por tipo de mascota' },
      series: [{
        name: 'Avisos',
        data: data
      }],
      accessibility: {
        point: { valueSuffix: ' avisos' }
      }
    });
  }

  function dibujarBarras(porMesYTipo) {
    const mesesSet = new Set(porMesYTipo.map(r => r.mes));
    const mesesOrdenados = Array.from(mesesSet).sort();

    function seriePara(tipoMascota) {
      return mesesOrdenados.map(mes => {
        const fila = porMesYTipo.find(r => r.mes === mes && r.tipo === tipoMascota);
        return fila ? fila.avisos : 0;
      });
    }

    const dataGato = seriePara('gato');
    const dataPerro = seriePara('perro');

    Highcharts.chart('chart-barras', {
      chart: { type: 'column' },
      title: { text: 'Avisos por mes (gatos vs perros)' },
      xAxis: {
        categories: mesesOrdenados,
        title: { text: 'Mes' }
      },
      yAxis: {
        min: 0,
        title: { text: 'Cantidad de avisos' }
      },
      series: [
        { name: 'Gatos', data: dataGato },
        { name: 'Perros', data: dataPerro }
      ]
    });
  }

  const datos = await cargarDatos();
  if (!datos) return;

  dibujarLinea(datos.avisos_por_dia);
  dibujarTorta(datos.total_por_tipo);
  dibujarBarras(datos.por_mes_y_tipo);
})();
