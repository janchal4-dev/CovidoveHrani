<?php
    include "mysql/datConn.php";
    
    //výběr všech dat z databáze
    $query = "SELECT * FROM users";

    $result = mysqli_query($connection,$query);

    if(!$result){
        die("Dotaz do databáze selhal".mysqli_error());
    }   



    // odeslání formuláře do databáze
    $minUsNameLength =3;
    $minPasLength =3;

    if(isset($_POST["userName"])){

      $userName = $_POST["userName"];
      $password = $_POST["password"];
    
      if(strlen($userName) >$minUsNameLength  && strlen($password) >$minUsNameLength){
        echo "Data have been sent!";
        echo "<br>";
    
    $query = "INSERT INTO users(username, password) VALUES('$userName', '$password')";
        $result = mysqli_query($connection,$query); 
        echo "<br>"; 
         echo $result; 
         header("Location: index.php");
    
    if(!$result){
      die(mysqli_error());
    }
      }}
      else{
        echo "The username length and password length must be at least" .$minUsNameLength ."characters";
      };
    
    
      // vypsání dat z databáze
    
      $query = "SELECT * FROM users";
      $result1 = mysqli_query($connection,$query); 
    
    
?>



<!DOCTYPE html>
<html lang="cz">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title></title>
  <link rel="stylesheet" href="style.css">
</head>

<body>





<form action="index.php" method="post">
  <br>
  <input type="text" name="userName" id="userName" placeholder="User Name">
  <br><br>
  <input type="password" name="password" id="password" placeholder="Password">
  <br><br>
  <input type="submit" value="Submit" id="submit">
</form>
<?php 

while($row = mysqli_fetch_assoc($result1)){
  print "<pre>";
  print_r($row);
  print"</pre>";
}


?>
  <script src="script.js"></script>

</script>
</body>
</html>
