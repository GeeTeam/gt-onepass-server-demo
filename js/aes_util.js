var CryptoJS = require("crypto-js");
var key ="32139f31fc733647b1e865ebaab277c2";
var iv = "0000000000000000";


function encrypt(text){
    var ciphertext = CryptoJS.AES.encrypt(text,CryptoJS.enc.Utf8.parse(key),{
        iv:CryptoJS.enc.Utf8.parse(iv),
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    return Buffer.from(ciphertext.toString(),'base64').toString("hex");
}

function decrypt(text){
    var result = CryptoJS.AES.decrypt(Buffer.from(text, 'hex').toString("base64"),CryptoJS.enc.Utf8.parse(key),{
        iv:CryptoJS.enc.Utf8.parse(iv),
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8)
}

var text="123";
var encoded=encrypt(text);
console.log(encoded);
console.log(decrypt(encoded));