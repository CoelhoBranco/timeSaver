<?php

#Start SW, if enabled.
if ($M->Config->system->PWA && $_SERVER["REQUEST_URI"] == "/sw") {
    header('Content-Type: application/javascript');
    echo file_get_contents("app/global/view/pages/sw.js", true);
    exit();
}

if ($_SERVER["REQUEST_URI"] == "/manifest") {
    header('Content-Type: application/manifest+json');
    include("app/global/view/pages/manifest.php");
    exit();
}

#Start loader, if enabled.
if ($M->Config->system->LOADER && !isset($_GET["loaded"])) {
    echo <<<loader
    <!DOCTYPE html>
    <html lang="{$M->Config->site->LANG}" dir="ltr">
    loader;

    @include("app/global/view/pages/loader.php");
    if ($M->Config->system->PWA) {
        echo <<<content
        <link rel="manifest" href="/manifest">
        <script>
            /* Only register a service worker if it's supported */
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/sw');
            }
        </script>
        content;
    }



    echo <<<loader
    <script>
        const params = new URLSearchParams(window.location.search);
        params.set('loaded', true);
        url = `\${window . location . pathname}?\${params}`;
        fetch(url)
            .then((response) => response.text())
            .then((page) => {
                document.querySelector("html").innerHTML = page;
            });
    </script>
    loader;
    exit();
}

#Turning errors into exceptions.
set_error_handler(function ($severity, $message, $filename, $lineno) {
    if (DEBUG) {
        exit("$message IN $filename IN line $lineno, SEVERITY = $severity");
        return false;
    }
    throw new ErrorException($message, 0, $severity, $filename, $lineno);
});

#Create function stream_resolve_include_path if not exist.
if (!function_exists('stream_resolve_include_path')) {
    function stream_resolve_include_path($filename)
    {
        $paths = PATH_SEPARATOR == ':' ?
            preg_split('#(?<!phar):#', get_include_path()) :
            explode(PATH_SEPARATOR, get_include_path());
        foreach ($paths as $prefix) {
            $ds = substr($prefix, -1) == DIRECTORY_SEPARATOR ? '' : DIRECTORY_SEPARATOR;
            $file = $prefix . $ds . $filename;

            if (file_exists($file)) {
                return $file;
            }
        }

        return false;
    }
}