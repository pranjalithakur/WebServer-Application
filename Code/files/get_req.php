<html>
<body>

<p>
<?php
$name = $_GET['name'];
$email = $_GET['email'];
echo "<b>Name: </b>" . $name . "<br>";
echo "<b>Email: </b>" . $email ;
?>
</p>
<br />

<p>
<?php
$cont = $_GET['cont'];
$file = fopen($cont, "r");
$display = fread($file, filesize($cont));
fclose($file);
echo "<b>File Contents: </b>" . $display
?>
</p>

</body>
<footer>
    <p><a href="get_req.html">GET page</a></p>
    <p><a href="index.html">Home Page</a></p>
</footer>

</html>

