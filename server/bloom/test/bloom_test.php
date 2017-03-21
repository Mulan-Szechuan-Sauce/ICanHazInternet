<?php
require_once('../bloom.php');
$foo = new Bloom(216553, 0.01);
echo $foo->get_size();
echo "\n";
echo $foo->get_runs();
echo "\n";

$bar = new Bloom(100000);
$bar->add("Test");
$bar->add("this");
$bar->add("bloom");
echo $bar->lookup("Test") . "\n";
echo $bar->lookup("foo") . "\n";
echo $bar->lookup("this") . "\n";
echo $bar->lookup("bar") . "\n";
echo $bar->lookup("bloom") . "\n";
echo $bar->lookup("Bloom") . "\n";
