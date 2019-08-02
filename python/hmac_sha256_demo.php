<?php 
$app_id = 'zoekwui1hnmg49x5fwzf5la0ml5dziwn';
$app_key = 'gywzffojtnzl0vd6kcut8fcgyud5wg49';
// $timestamp = (string)time();
$timestamp = '1542355862990';
$secret = $app_id . '&&' . $timestamp;
$s = hash_hmac('sha256', $secret, $app_key, true);
echo bin2hex($s);
 ?>