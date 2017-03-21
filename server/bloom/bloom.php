<?php
require_once('murmurhash3.php');
class Bloom {
    private $arr;
    private $size;
    private $runs;

    function __construct($num_items, $false_per=0.01) {
        $this->size = (int)ceil(-$num_items*log($false_per) / pow(log(2), 2));
        $this->runs = (int)ceil(($this->size/$num_items) * log(2));
        $this->arr = new SplFixedArray($this->size);

        //$this->size = $s;
        //$this->runs = $r;
    }

    private function hash($thing, $seed) {
        return murmurhash3($thing, $seed);
    }

    function add($thing) {
        $result = $thing;
        foreach (range(0, $this->runs) as $seed) {
            $result = fmod(hexdec(sha1($result)), $this->size);
            $result = fmod(hexdec(md5($result)), $this->size);
            $result = murmurhash3($result, $seed) % $this->size;
            $this->arr[$result] = 1;
        }
    }

    function lookup($thing) {
        $result = $thing;
        foreach (range(0, $this->runs) as $seed) {
            $result = fmod(hexdec(sha1($result)), $this->size);
            $result = fmod(hexdec(md5($result)), $this->size);
            $result = murmurhash3($result, $seed) % $this->size;
            if ($this->arr[$result] == 0) return 0;
            else return 1;
        }
    }

    function show_list() {
        print_r($this->arr);
    }

    function get_size() {
        return $this->size;
    }

    function get_runs() {
        return $this->runs;
    }
}

