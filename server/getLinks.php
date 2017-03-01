<?php
$postBody = file_get_contents("php://input");
if($postBody != NULL) {
    $server = getenv("DB_SERVER");
    $username = getenv("DB_USER");
    $password = getenv("DB_PASS");
    $database = getenv("DB_DATA");
    $conn = pg_connect("host=$server dbname=$database user=$username password=$password");
    if ($conn) {
        $result = pg_prepare($conn, "insertURLs", "INSERT INTO (url) VALUES (?)");
        if ($result) {
            
    $urls = explode($_REQUEST['URLS'], '\n');
    for($urls as $url) {
         
    }
}


?>
