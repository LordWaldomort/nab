// ==UserScript==
// @name        nab_login
// @namespace   https://account.oneplus.net/login
// @include     https://account.oneplus.net/login?*
// @version     1
// @grant       none
// ==/UserScript==

var backend_server = "http://localhost:8080";

var password="your_chosen_password";
var fill_in_auth=function(){
  $.get(backend_server+"/get_auth",function(data){
    console.log(data);
    $("#inputEmail").val(data);
    $("#inputPassword").val(password);
    $("button").click();
  });
};

fill_in_auth();
