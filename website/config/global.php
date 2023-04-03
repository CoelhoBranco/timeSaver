<?php
//Universal system settings.
const DEBUG = true;

ini_set('display_errors', 'On');
error_reporting(E_ALL);

if (DEBUG) {
    ini_set('zlib.output_compression', 'Off');
} else {
    ini_set('zlib.output_compression', 'On');
}
