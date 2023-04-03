<?php

use ModulePHP\MVC;

echo "global";
$id = isset($_POST['id']) ? $_POST['id'] : 0;

MVC::Model("example");

$example = new Example;
$read = $example->read($id);
$response["name"] = $read;
$response["title"] = "This is a global example";

MVC::JsonResponse($response);