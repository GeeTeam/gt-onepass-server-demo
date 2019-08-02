$encryptMethod = 'aes-256-cbc';
$iv = '0000000000000000';
$app_key = 'gywzffojtnzl0vd6kcut8fcgyud5wg49';
$encode_phone_str = 'be28dea08ee543320b1ef9e1bceb51e4';
$res = openssl_decrypt(hex2bin($encode_phone_str), $encryptMethod, $app_key, 1, $iv);
echo $res;