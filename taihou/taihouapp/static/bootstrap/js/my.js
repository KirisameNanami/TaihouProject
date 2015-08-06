$('#RegistEmail').blur(function(){
    if($('#RegistEmail').val()=='')
    {
        $('.RegistLabel')[0].innerHTML='&gt;&gt;&gt;Availability Test&lt;&lt;&lt;';
        return;
    }
    $('.RegistLabel')[0].innerHTML='&gt;&gt;&gt;Checking....&lt;&lt;&lt;';
    $.post(
                '/check/',
                {
                    'Name':$('#RegistEmail').val()
                },
                function(result){
                    $('.RegistLabel')[0].innerHTML=result;
                    if(result[0]!='S'){
                        $('.Register').slideDown('fast');
                        $('.Register label.RegistLabel')[0].innerHTML='Click here to get '+$('#RegistEmail').val()+'@taihou.moe !';
                    }
                });
});

$('.Register label.RegistLabel').click(function(){
    $('.Register label.RegistLabel')[0].innerHTML='&gt;&gt;&gt;Creating your account...&lt;&lt;&lt;';
    $.post(
                '/create/',
                {
                    'Name':$('#RegistEmail').val()
                },
                function(result){
                    if(result[0]=='S'){
                        $('.Login label.RegistLabel')[0].innerHTML=result;
                        $('.RegistLabel')[0].innerHTML='REMEMBER TO CHANGE YOUR PASSWORD AT ONCE.';
                        $('.Register').slideUp('fast');
                        $('.Login').slideDown('fast');
                    }else{
                        $('Register label.RegistLabel')[0].innerHTML=result;
                    }
                });
});

$('.Login label.RegistLabel').click(function(){
    $('.Login label.RegistLabel')[0].innerHTML='Please wait for a moment...';
    $.post(
                '/login/',
                {
                    'Name':$('#RegistEmail').val()
                },
                function(result){
                    if(result=='Exist')return;
                    window.open(window.location+'clicklogin/?Name='+$('#RegistEmail').val()+'&auth='+result);
                });
});
