<?php
require_once('mururhash3.php');

class Bloom {
    private $arr;
    private $size;

    function __construct() {
        $argv = func_get_args();
        $argc = func_num_args();

        echo $argc;
    }
}
?>
