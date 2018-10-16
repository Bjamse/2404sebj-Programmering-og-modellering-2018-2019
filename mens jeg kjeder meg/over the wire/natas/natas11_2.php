#!/usr/bin/php
<?php
function xor_encrypt($in, $key) {

    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$plaintext = json_encode($defaultdata);
$cifer = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSQwx+RUEOaAw=");

#print(xor_encrypt($plaintext, $cifer));
#print("\n\n\n");

$good_key = "qw8J";
$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$good_plain = json_encode($good_data);
$good_cifer = base64_encode(xor_encrypt($good_plain,$good_key));

printf($good_cifer."\n");
?>

// File contains code to help solve natas 11, was not capable of finding the flag without this.