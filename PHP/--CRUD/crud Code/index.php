<?php
include 'funciones.php';

csrf();
if (isset($_POST['submit']) && !hash_equals($_SESSION['csrf'], $_POST['csrf'])) {
  die();
}

$error = false;
$config = include 'config.php';

try {
  $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
  $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);

  if (isset($_POST['author'])) {
    $consultaSQL = "SELECT * FROM stock WHERE author LIKE '%" . $_POST['author'] . "%'";
  } else {
    $consultaSQL = "SELECT * FROM stock";
  }

  $sentencia = $conexion->prepare($consultaSQL);
  $sentencia->execute();

  $book = $sentencia->fetchAll();

} catch(PDOException $error) {
  $error= $error->getMessage();
}

$titulo = isset($_POST['author']) ? 'Lista de book (' . $_POST['author'] . ')' : 'Lista de libros';
?>

<?php include "templates/header.php"; ?>

<?php
if ($error) {
  ?>
  <div class="container mt-2">
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-danger" role="alert">
          <?= $error ?>
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
      <a href="crear.php"  class="btn btn-primary mt-4">Nuevo Libro</a>
      <hr>
      <form method="post" class="form-inline">
        <div class="form-group mr-3">
          <input type="text" id="author" name="author" placeholder="Buscar por author" class="form-control">
        </div>
        <input name="csrf" type="hidden" value="<?php echo escapar($_SESSION['csrf']); ?>">
        <button type="submit" name="submit" class="btn btn-primary">Ver resultados</button>
      </form>
    </div>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h2 class="mt-3"><?= $titulo ?></h2>
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>name</th>
            <th>author</th>
            <th>year</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <?php
          if ($book && $sentencia->rowCount() > 0) {
            foreach ($book as $fila) {
              ?>
              <tr>
                <td><?php echo escapar($fila["id"]); ?></td>
                <td><?php echo escapar($fila["name"]); ?></td>
                <td><?php echo escapar($fila["author"]); ?></td>
                <td><?php echo escapar($fila["year"]); ?></td>
                <td>
                  <a href="<?= 'borrar.php?id=' . escapar($fila["id"]) ?>">🗑️Borrar</a>
                  <a href="<?= 'editar.php?id=' . escapar($fila["id"]) ?>">✏️Editar</a>
                </td>
              </tr>
              <?php
            }
          }
          ?>
        <tbody>
      </table>
    </div>
  </div>
</div>

<?php include "templates/footer.php"; ?>