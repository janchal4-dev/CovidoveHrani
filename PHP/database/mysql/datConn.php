<?php

        // připojení do databáze
        $connection = mysqli_connect("localhost","root","","loginapplication");
        
        if($connection){
            echo "Jsme propojení s databází";
            echo "<br>";
            echo "<a href=update.php>Update.php</a>";
            echo "-------------------";
            echo "<a href=index.php>Index.php</a>";
            echo "<br>";
        } else {
            die("Ou, něco se pokazilo");
        }

        
?>