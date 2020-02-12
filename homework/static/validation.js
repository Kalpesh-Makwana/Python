$(document).ready(function(){

    // For Login Contact Number
    $("#error").css("color", "red");
    
    $('#id_contact').blur(function(){
        len=$('#id_contact').val()
        var con= /^[0-9]*$/
        if(len.length>10 || len.length<10 ){
            $('#error').html("* Enter Contact Number Must be 10 digit")
        }else if(!con.test(len)){
            $('#error').html("* Enter Contact Number Must be digit not a character")
        }else{
            $('#error').html("")
        }
    });

    //For Login Password
    $('#id_password').blur(function(){
        pass=$('#id_password').val()   
        if(pass.length<=0){
            $('#error').html("*Password should not be blank")
        }else{
            $('#error').html("")
        }
    });

    //For First Name
    $('#id_first_name').blur(function(){
        len=$('#id_first_name').val()
        var expr= /^[a-zA-Z_]*$/
        
        if(!expr.test(len)){
            $('#error').html("* First name must be character, Special character are not allowed!")
            return false
        }else if(len==0)
        {
            $('#error').html("* First name must be not be blank!")
            return false
        }
        else{
            $('#error').html("")
            return true
        }
    });

     //For Last Name
     $('#id_last_name').blur(function(){
        len=$('#id_last_name').val()
        var expr= /^[a-zA-Z_]*$/
        
        if(!expr.test(len)){
            $('#error').html("* Last name must be character, Special character are not allowed!")
            return false
        }else if(len==0)
        {
            $('#error').html("* Last name must be not be blank!")
            return false
        }
        else{
            $('#error').html("")
            return true
        }
    });

    //For Email
    $('#id_email').blur(function(){
        
        len=$('#id_email').val()
        var expr= /^[a-zA-Z_.0-9]+@[a-zA-Z]+[.]{1}[a-zA-Z]+$/
        
        if(!expr.test(len)){
            $('#error').html("* Please enter proper email !")
            return false
        }else if(len==0)
        {
            $('#error').html("* Plase Enter Email")
            return false
        }
        else{
            $('#error').html("")
            return true
        }
    });

    //Registration Password and Confirm Password
    $('#id_password2').blur(function(){
        pass1=$('#id_password1').val() 
        pass2=$('#id_password2').val()   
        if(pass1.length<=0 | pass2.length<=0){
            $('#error').html("* Password should not be blank")
            return false
        }else if(pass1.length<8 | pass2.length<8){
            $('#error').html("* Password Minimum length must be 8")
            return false
        }
        else if(pass1!=pass2){
            $('#error').html("* Password Not Matching")
            return false
        }

        else{
            $('#error').html("")
            return true
        }
    });

    //Login Submit 
    $("#submitform").submit(function(e){
        //e.preventDefault();
    });

});