<?php
    //připojení do databáze
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
    
    if(isset($_POST["submit"])){
        $username = $_POST["username"];
        $password = $_POST["password"];
        $id = $_POST["id"];

        if(strlen($username) >$minUsNameLength  && strlen($password) >$minUsNameLength){
          echo "Data have been sent!";
          echo "<br>";

        $query2 = "UPDATE users SET username='$username', password='$password' WHERE id = $id ";
    
        $result2 = mysqli_query($connection,$query2);

        if(!$result2){
            die("Query selhalo ".mysqli_error());
        }
            
        }}
    else{
    echo "The username length and password length must be at least" .$minUsNameLength ."characters";
  };

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




<form action="update.php" method="post">
        <input type="text" name="username" id="userName" placeholder="User Name"><br><br>
        <input type="password" name="password" id="password" placeholder="Password"><br><br>
        
        <select name="id" id="">
           <?php
            while($row = mysqli_fetch_assoc($result)){
               $id = $row["id"];
               echo "<option value='$id'>$id</option>"; 
            }
            ?>
        </select>
        
        <input type="submit" name="submit" value="Submit" id="submit">
    </form>


  <script src="script.js"></script>

</script>
</body>
</html>

