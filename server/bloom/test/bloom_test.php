<?php
require_once('../bloom.php');
$foo = new Bloom(216553, 0.01);
echo $foo->get_size();
echo "\n";
echo $foo->get_runs();
