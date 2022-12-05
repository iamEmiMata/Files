<?php
include 'funciones.php';

csrf();
if (isset($_POST['submit']) && !hash_equals($_SESSION['csrf'], $_POST['csrf'])) {
  die();
}

$config = include 'config.php';

$resultado = [
  'error' => false,
  'mensaje' => ''
];

if (!isset($_GET['id'])) {
  $resultado['error'] = true;
  $resultado['mensaje'] = 'El author no existe';
}

if (isset($_POST['submit'])) {
  try {
    $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
    $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);

    $book = [
      "id"        => $_GET['id'],
      "name"    => $_POST['name'],
      "author"  => $_POST['author'],
      "year"     => $_POST['year']
    ];
    
    $consultaSQL = "UPDATE stock SET
        name = :name,
        author = :author,
        year = :year
        WHERE id = :id";
    $consulta = $conexion->prepare($consultaSQL);
    $consulta->execute($book);

  } catch(PDOException $error) {
    $resultado['error'] = true;
    $resultado['mensaje'] = $error->getMessage();
  }
}

try {
  $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
  $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);
    
  $id = $_GET['id'];
  $consultaSQL = "SELECT * FROM stock WHERE id =" . $id;

  $sentencia = $conexion->prepare($consultaSQL);
  $sentencia->execute();

  $book = $sentencia->fetch(PDO::FETCH_ASSOC);

  if (!$book) {
    $resultado['error'] = true;
    $resultado['mensaje'] = 'No se ha encontrado el libro';
  }

} catch(PDOException $error) {
  $resultado['error'] = true;
  $resultado['mensaje'] = $error->getMessage();
}
?>

<?php require "templates/header.php"; ?>

<?php
if ($resultado['error']) {
  ?>
  <div class="container mt-2">
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-danger" role="alert">
          <?= $resultado['mensaje'] ?>
        </div>
      </div>
    </div>
  </div>
  <?php
}
?>

<?php
if (isset($_POST['submit']) && !$resultado['error']) {
  ?>
  <div class="container mt-2">
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-success" role="alert">
          El libro ha sido actualizado correctamente
        </div>
      </div>
    </div>
  </div>
  <?php
}
?>

<?php
if (isset($book) && $book) {
  ?>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h2 class="mt-4">Editando el libro <?= escapar($book['name']) . ' ' . escapar($book['author'])  ?></h2>
        <hr>
        <form method="post">
          <div class="form-group">
            <label for="name">name</label>
            <input type="text" name="name" id="name" value="<?= escapar($book['name']) ?>" class="form-control">
          </div>
          <div class="form-group">
            <label for="author">author</label>
            <input type="text" name="author" id="author" value="<?= escapar($book['author']) ?>" class="form-control">
          </div>
          <div class="form-group">
            <label for="year">year</label>
            <input type="year" name="year" id="year" value="<?= escapar($book['year']) ?>" class="form-control">
          </div>
          <div class="form-group">
            <input name="csrf" type="hidden" value="<?php echo escapar($_SESSION['csrf']); ?>">
            <input type="submit" name="submit" class="btn btn-primary" value="Actualizar">
            <a class="btn btn-primary" href="index.php">Regresar al inicio</a>
          </div>
        </form>
      </div>
    </div>
  </div>
  <?php
}
?>

<?php require "templates/footer.php"; ?>