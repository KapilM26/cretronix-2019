$(document).ready(function(){
    //Hide all questions
    $('.questionform').hide();
    //Show first question
    $('#q1').show();
    
    $('#q1 #next').click(function(){
        $('.questionform').hide();
        $('#q2').fadeIn(300);
        return false;
    });
    $('#q2 #back').click(function(){
        $('.questionform').hide();
        $('#q1').fadeIn(300);
        return false;
    });
    
    $('#q2 #next').click(function(){
        $('.questionform').hide();
        $('#q3').fadeIn(300);
        return false;
    });
    $('#q3 #back').click(function(){
        $('.questionform').hide();
        $('#q2').fadeIn(300);
        return false;
    });
    
    

    
 
    
    
    
    
    
    
    
});