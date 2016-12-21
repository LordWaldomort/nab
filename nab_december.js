// ==UserScript==
// @name         nab_december
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @include      https://oneplusstore.in/december?*
// @grant        none
// ==/UserScript==


var my_mobile_number = 'my_mobile_here';
var backend_server = "http://localhost:8080";
gen_random_phone = function(){
    phone_string = "7";
    for(i = 0; i < 9; i++)
        phone_string += Math.floor(Math.random()*10);
    return phone_string;
};
if($("#diwali-login-btn").children("i").length===0){
    $("#diwali-login-btn").children("a")[0].click();
}else{

	var target_number= gen_random_phone();

	$.ajax({url:"https://oneplusstore.in/xman/jubilee/ticket/update?event=mobile"}).done(function(data){
		$.ajax({url:"https://account.oneplus.net/json/user/check-mobile",type:"post", data: {mobile: target_number},dataType: "json",xhrFields: {withCredentials: !0},timeout: 3e4,}).done(function() {
			$.ajax({url:"https://account.oneplus.net/json/user/send-sms",data:{mobile:target_number},type:"post",dataType:"json",xhrFields:{withCredentials:!0},timeout:3e4,}).done(function() {
				$.ajax({url:"https://account.oneplus.net/json/user/send-sms",data:{mobile:my_mobile_number},type:"post",dataType:"json",xhrFields:{withCredentials:!0},timeout:3e4,});
			});
		});
	});

	$.ajax({url:backend_server+"/request_otp?num=" + target_number}).done(function(data){
        console.log(data);
        $.ajax({url:"https://account.oneplus.net/json/user/bind-mobile",type:"post",data:{code:data,countryCode:"in",mobile:target_number},dataType:"json",xhrFields:{withCredentials:!0},timeout:3e4,}).done(function(data){
            console.log(data);
            $.ajax({url:"https://oneplusstore.in/xman/jubilee/ticket/update?event=mobile"}).done(function(data){
                console.log(data);
                $("#logOutBtn")[0].click();
            });
        });
    });
}
