<?php
require_once('murmurhash3.php');
class Bloom {
    private $arr;
    private $size;
    private $runs;

    function __construct($s, $r) {
        $this->size = $s;
        $this->arr = new SplFixedArray($s);
        $this->runs = $r;
    }

    function getSize() {
        return $this->size;
    }

    private function hash($thing, $seed) {
        return murmurhash3($thing, $seed);
    }

    function add($thing) {
        $result = $thing;
        foreach (range(0, $this->runs) as $seed) {
            $result = murmurhash3($result, $seed) % $this->size;
            $this->arr[$result] = 1;
        }
    }

    function lookup($thing) {
        $result = $thing;
        foreach (range(0, $this->runs) as $seed) {
            $result = murmurhash3($result, $seed) % $this->size;
            if ($this->arr[$result] == 0) return 0;
            else return 1;
        }
    }
}

