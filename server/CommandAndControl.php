<?php
class CommandAndControlServer {
    private $URLsToCheck;
    private $numClients;
    private $

    function __construct($numClients) {
        $this->URLsToCheck = array();
        $this->numClients = $numClients;
    }

    function addURL($url) {
        $this->URLsToCheck[] = $url;
    }

    function getURLs() {
        if(empty($this->URLsToCheck))
            return NULL;
        // TODO: Divide by number of connected clients?
        $numURLsToGive = ceil(sizeof($this->URLsToCheck)/$this->numClients);
        $nextBatch = array_slice($this->URLsToCheck, 0, $numURLsToGive);
        return formatURLs($nextBatch);
    }

    private function formatURLs($toFormat) {
        $formattedString = "";
        for($toFormat as $URL) {
            $formattedString += $URL + '\n';
        }
        return $formattedString;
    }

}

?>
