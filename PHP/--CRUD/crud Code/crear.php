<?php

include 'funciones.php';

csrf();
if (isset($_POST['submit']) && !hash_equals($_SESSION['csrf'], $_POST['csrf'])) {
  die();
}

if (isset($_POST['submit'])) {
  $resultado = [
    'error' => false,
    'mensaje' => 'El libro' . escapar($_POST['name']) . ' ha sido agregado con éxito'
  ];

  $config = include 'config.php';

  try {
    $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
    $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);

    $book = [
      "name"   => $_POST['name'],
      "author" => $_POST['author'],
      "year"    => $_POST['year'],
    ];

    $consultaSQL = "INSERT INTO stock (name, author, year)";
    $consultaSQL .= "values (:" . implode(", :", array_keys($book)) . ")";

    $sentencia = $conexion->prepare($consultaSQL);
    $sentencia->execute($book);

  } catch(PDOException $error) {
    $resultado['error'] = true;
    $resultado['mensaje'] = $error->getMessage();
  }
}
?>

<?php include 'templates/header.php'; ?>

<?php
if (isset($resultado)) {
  ?>
  <div class="container mt-3">
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-<?= $resultado['error'] ? 'danger' : 'success' ?>" role="alert">
          <?= $resultado['mensaje'] ?>
        </div>
      </div>
    </div>
  </div>
  <?php
}
?>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h2 class="mt-4">Nuevo Libro</h2>
      <hr>
      <form method="post">
        <div class="form-group">
          <label for="name">name</label>
          <input type="text" name="name" id="name" class="form-control">
        </div>
        <div class="form-group">
          <label for="author">author</label>
          <input type="text" name="author" id="author" class="form-control">
        </div>
        <div class="form-group">
          <label for="year">year</label>
          <input type="year" name="year" id="year" class="form-control">
        </div>
        <div class="form-group">
          <input name="csrf" type="hidden" value="<?php echo escapar($_SESSION['csrf']); ?>">
          <input type="submit" name="submit" class="btn btn-primary" value="Enviar">
          <a class="btn btn-primary" href="index.php">Regresar al inicio</a>
        </div>
      </form>
    </div>
  </div>
</div>

<?php include 'templates/footer.php'; ?>