<?php
require_once('../bloom.php');
$foo = new Bloom(20, 2);
$foo->add("hi");
$foo->add("there");
echo $foo->lookup("boop");
echo $foo->lookup("hi");
echo $foo->lookup("hi");
echo $foo->lookup("there");
echo $foo->lookup("blarb");
