<?php
require_once('../bloom.php');
$num_words = 354984;

$bloom = new Bloom($num_words, 0.0001);
echo $bloom->get_size();
echo "\n";
echo $bloom->get_runs();
echo "\n";

$handle = fopen("words.txt", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        $bloom->add(trim($line));
    }
    fclose($handle);
}

while (1) {
    $temp = readline('> ');
    if ($bloom->lookup(trim($temp))) {
        echo "Yes!\n";
    } else {
        echo "No\n";
    }
}
