<?php 

include 'tools/toDo/crear.php';
include 'tools/toDo/listar.php';
// include 'tools/toDo/borrar.php';
?>



<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Desptok</title>
	<link rel="stylesheet" href="css/style.css">
</head>
<body>
	<header>
		<section>
			<h4>Hola Emi!</h4>
		</section>
		<ul>
			<li><a href="account.html">Cuenta</a></li>
			<li><a href="../index.html">Salir</a></li>
		</ul>
	</header>
	<main>
		<section class="sect">
			<section class="date">
				<h2 id="diaS"></h2>
				<h4 id="fecha"></h4>
				<h2 id="time"></h2>
			</section>
			<section class="text-form">
				<section class="texto">
					<span>Me encanta que no tengo una imagen falsa que mantener.
					Lo que ves es lo que hay. Algunos dias soy increble, otros dias soy un desastre, pero todos los dias soy yo.</span>
				</section>
				<section class="form">

					<label for="">Desptok</label>
					<form method="post">
						<label for="tasks"></label>
						<input type="text" id="tasks" name="tasks" placeholder="Nueva tarea" value="">
						<input name="csrf" type="hidden" value="<?php echo escapar($_SESSION['csrf']); ?>">
          				<input type="submit" name="submit" id="addTarea" value="Enviar" onclick="addTarea()">
					</form>
				</section>
			</section>
		</section>
		<section class="sect">
			<section class="sects">
				<section class="calendar">
					<section class="header">
						<a href='#' class="prev" id="prev">
			                <
			            </a>
			            <section class="currentDate">
			                <h4 id="month" class="month"></h4>
			                <h4 id="year" class="year"></h4>
			            </section>
			            <a href='#' class="next" id="next">
			                >
			            </a>
					</section>
					<section class="week">
			            <div id="calendarDays" class="items"></div>
			            <div id="daysGrid" class="items"></div>
			        </section>
				</section>

				<section class="pomodoro">
					<h5>Pomodoro</h5>
					<section class="timer">
						<h2>15:00</h2>
						<a href="#">Inicio</a>
					</section>
				</section>
			</section>
			<section class="tasks">
				<?php
			        if ($listar && $sentencia->rowCount() > 0) {
			        foreach ($listar as $fila) {
			    ?>
				<section class="lista" id="listaTarea">
					<section class="valueTasks" id="listaTarea">
						<input type='checkbox' class='check'>
						<input type="text" rows='2' value="<?php echo escapar($fila["tasks"]); ?>" readonly>
		                <a href="<?= 'editar.php?id=' . escapar($fila["id"]) ?>" title='Modificar'>✏️</a>
		                <a href="<?= 'tools/toDo/borrar.php?id=' . escapar($fila["id"]) ?>" title='Eliminar'>🗑️</a>
					</section>
				</section>
				 <?php
		            }
		          }
		          ?>
			</section>
		</section>
	</main>

	<?php

	if (isset($resultado)) {
	  ?>
		<section class="<?= $resultado['error'] ? 'info' : 'success';  ?>" role="alert">
			<section id="msg">
				<?=  $resultado['mensaje'] ?>	
			</section>
		</section>
	  <?php
	} else {
		?>
		<section class="info" role="alert">
			<section id="msg">
				Your list have been modify successfully!
			</section>
		</section>
		<?php
	}
	?>

	<footer>
		Website done by <strong>Emi Mata</strong>
		<a href="#">● Instagram : <b>_emimata</b></a>
		<a href="#">● <b>Github</b></a>
	</footer>
	<script src="tools/date/date.js"></script>
</body>
</html>