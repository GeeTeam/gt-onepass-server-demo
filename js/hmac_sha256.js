var CryptoJS = require("crypto-js");

function hmac_sha256(key) {
    var encrypto = CryptoJS.HmacSHA256("97639e105c9d4db9a9d9ac3787870168&&1563876938135", key);
    var base64 = CryptoJS.enc.Base64.stringify(encrypto);
    return Buffer.from(base64.toString(),'base64').toString("hex")
}


console.log(hmac_sha256('32139f31fc733647b1e865ebaab277c2'));
