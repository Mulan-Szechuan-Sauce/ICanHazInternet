<?php
$postBody = file_get_contents("php://input");
if($postBody != NULL) {
    $conn = pg_connect();
    $urls = explode($_REQUEST['URLS'], '\n');
    for($urls as $url) {
         
    }
}


?>
