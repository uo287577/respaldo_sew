<?php 
	class Carrusel
	{
		protected $nombrePais;
		protected $nombreCapital;

		public function __construct($nombrePais, $nombreCapital)
		{
			$this -> nombrePais = $nombrePais;
			$this -> nombreCapital = $nombreCapital;
		}

		public function cargarFotosCarrusel()
		{
			$tags = $this -> nombreCapital;
			$numeroFotosMaximo = 10;

			$url = 'https://api.flickr.com/services/feeds/photos_public.gne?'
				.'&tags='.$tags
				.'&per_page='.$numeroFotosMaximo
				.'&format=json'
				.'&nojsoncallback=1';

			$jsonResultante = json_decode(file_get_contents($url));
			if($jsonResultante)
			{
				for($i = 0; $i < $numeroFotosMaximo; $i++)
				{
					$item = $jsonResultante -> items[$i];

					$titulo = $item -> title;
					$contenido = $item -> media -> m;
					
					echo "<img src='" . $contenido . "' alt='" . $titulo . "' loading='lazy' />";
				}
			} else
			{
				echo "<p>Error en la decodificación del carrusel</p>";
			}

		}
	}
?>

<!DOCTYPE HTML>

<html lang="es">
<head>
    <!-- Datos que describen el documento -->
    <meta charset="UTF-8" />
    <title>F1 Desktop viajes</title>
	
	<meta name ="author" content="Miguel Fernández Huerta" />
	<meta name="description" content="Documento que recoge información acerca de los viajes de la F1" />
	<meta name ="keywords" content ="Viajes,viajes,Viaje,viaje" />
	<meta name ="viewport" content ="width=device-width, initial-scale=1.0" />

	<!-- añadir el elemento link de enlace a la hoja de estilo dentro del <head> del documento html -->
	<link rel="stylesheet" type="text/css" href="../estilo/estilo.css" />
	<link rel="stylesheet" type="text/css" href="../estilo/layout.css" />
	<link rel="icon" href="../multimedia/imagenes/favicon.ico" />
	<link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/v2.11.0/mapbox-gl.css" />

	<script src="../js/viajes.js"></script>
	<script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
	<script src="https://api.mapbox.com/mapbox-gl-js/v3.7.0/mapbox-gl.js" defer></script>
</head>

<body>
	<header>
    	<!-- Datos con el contenidos que aparece en el navegador -->
    	<h1><a href="../index.html" title="Enlace a la página principal">F1 Desktop</a></h1>
		<nav>
			<a href="../index.html" title="Inicio F1 Desktop">Inicio</a>
			<a href="../piloto.html" title="Pestaña del piloto">Piloto</a>
			<a href="../noticias.html" title="Pestaña de noticias">Noticias</a>
			<a href="../calendario.html" title="Pestaña de calendario">Calendario</a>
			<a href="../meteorologia.html" title="Pestaña de metereologia">Metereologia</a>
			<a href="../circuito.html" title="Pestaña de circuito">Circuito</a>
			<a href="./viajes.php" title="Pestaña de viajes" class="active">Viajes</a>
			<a href="../juegos.html" title="Pestaña de juegos">Juegos</a>
		</nav>
	</header>

	<!-- Migas -->
	<p>Estás en: Inicio >> Viajes</p>

	<main>
	    <h2>Viajes de la F1</h2>
		<p></p>

		<article>
    		<h3>Carrusel de Imágenes</h3>
			<?php 
				$carrusel = new Carrusel("España","Barcelona");
				$carrusel -> cargarFotosCarrusel();
			?>
  
  			<!-- Control buttons -->
  			<button> &gt; </button>
  			<button> &lt; </button>
		</article>


		<input type="button" value="Obtener mapa estático" onclick="viajes.cargarMapaEstatico();" />
		<script>
			var viajes = new Viajes();
			viajes.crearCarrusel();
		</script>
	</main>

</body>
</html>