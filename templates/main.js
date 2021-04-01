/**
 * This javascript will mainly be used for the comment generator.
 * The original js file is different from the js file you can see in the browser
 * The JS file uses Jinja2 template rendering to duplicate similar functions with other indices.
 */

$(document).ready(function(){
//js for intro.html aka /intro
$(window).on('load', function() {
    $('#intro_modal').modal('show');
});
//js for main.html aka /
$("#copy_comment").click(function(){
    //  function is used to to copy text in a textarea
    $("#all_comments").select();
    $('#toast1').toast('show');
    $("#all_comments").select();
    document.execCommand("copy");
});
$("#save_comment").click(function(){
    // this function will store the text in the browser
    $('#toast2').toast('show');
    var text = $('#all_comments').val();
    localStorage.setItem('draft', text);
});
$("#open_last_save").click(function(){
    // this function will open the text saved in the browser
    $('#toast3').toast('show');
    var stored_draft = localStorage.getItem('draft');
    $('#all_comments').val(stored_draft);
});
{% for element in requirements %}
{% if element[6] == 1 %}
$("#add-comment-written{{ requirements.index(element) }}").click(function(){
    // this function will add text from the select tag to the textarea above
    var $result = $("#all_comments");
    var comment = $("#select_written_{{ requirements.index(element) }}").val();
    if (comment != null){
    $result.val($result.val() + comment + " ");}
});

$('#written_form_{{ requirements.index(element) }}').change(function(){
    // this function will check the grade of excellence value and show the comments belonging to them
    var selected_value = $("input[name='written_optradio{{ requirements.index(element) }}']:checked").val();
    switch(selected_value) {
      case '1':
            var written_comment1 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 1|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_written_{{ requirements.index(element) }}").empty();
            $.each( written_comment1, function( index, value ) {
                // this function will add all the values corresponding with the number 1 (best comments)
                $("#select_written_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '2':
            var written_comment2 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 2|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_written_{{ requirements.index(element) }}").empty();
            $.each( written_comment2, function( index, value ) {
                // this function will add all the values corresponding with the number 2 (good comments)
                $("#select_written_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '3':
            var written_comment3 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 3|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_written_{{ requirements.index(element) }}").empty();
            $.each( written_comment3, function( index, value ) {
                // this function will add all the values corresponding with the number 3 (bad comments)
                $("#select_written_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '4':
            var written_comment4 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 4|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_written_{{ requirements.index(element) }}").empty();
            $.each( written_comment4, function( index, value ) {
                // this function will add all the values corresponding with the number 4 (worst comments)
                $("#select_written_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
    }
});
{% endif %}
{% if element[7] == 1 %}
$("#add-comment-math{{ requirements.index(element) }}").click(function(){
    // this function will add text from the select tag to the textarea above
    var $result = $("#all_comments");
    var comment = $("#select_math_{{ requirements.index(element) }}").val();
    if (comment != null){
    $result.val($result.val() + comment + " ");}
});

$('#math_form_{{ requirements.index(element) }}').change(function(){
    // this function will check the grade of excellence value and show the comments belonging to them
    var selected_value = $("input[name='math_optradio{{ requirements.index(element) }}']:checked").val();
    switch (selected_value) {
      case '1':
            var math_comment1 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 1|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_math_{{ requirements.index(element) }}").empty();
            $.each( math_comment1, function( index, value ) {
                // this function will add all the values corresponding with the number 1 (best comments)
                $("#select_math_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '2':
            var math_comment2 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 2|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_math_{{ requirements.index(element) }}").empty();
            $.each( math_comment2, function( index, value ) {
                // this function will add all the values corresponding with the number 2 (good comments)
                $("#select_math_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '3':
            var math_comment3 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 3|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_math_{{ requirements.index(element) }}").empty();
            $.each( math_comment3, function( index, value ) {
                // this function will add all the values corresponding with the number 3 (bad comments)
                $("#select_math_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
      case '4':
            var math_comment4 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 4|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
            $("#select_math_{{ requirements.index(element) }}").empty();
            $.each( math_comment4, function( index, value ) {
                // this function will add all the values corresponding with the number 4 (worst comments)
                $("#select_math_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
            });
            break;
    }
});

{% endif %}
{% if element[8] == 1 %}
$("#add-comment-prog{{ requirements.index(element) }}").click(function(){
    // this function will add text from the select tag to the textarea above
    var $result = $("#all_comments");
    var comment = $("#select_prog_{{ requirements.index(element) }}").val();
    if (comment != null){
    $result.val($result.val() + comment + " ");}
});

$('#prog_form_{{ requirements.index(element) }}').change(function(){
    // this function will check the grade of excellence value and show the comments belonging to them
    var selected_value = $("input[name='prog_optradio{{ requirements.index(element) }}']:checked").val();
    switch (selected_value) {
      case '1':
        var prog_comment1 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 1|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
        $("#select_prog_{{ requirements.index(element) }}").empty();
        $.each( prog_comment1, function( index, value ) {
            // this function will add all the values corresponding with the number 1 (best comments)
            $("#select_prog_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
        });
        break;
      case '2':
        var prog_comment2 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 2|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
        $("#select_prog_{{ requirements.index(element) }}").empty();
        $.each( prog_comment2, function( index, value ) {
            // this function will add all the values corresponding with the number 2 (good comments)
            $("#select_prog_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
        });
        break;
      case '3':
        var prog_comment3 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 3|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
        $("#select_prog_{{ requirements.index(element) }}").empty();
        $.each( prog_comment3, function( index, value ) {
            // this function will add all the values corresponding with the number 3 (bad comments)
            $("#select_prog_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
        });
        break;
      case '4':
        var prog_comment4 = [{% for val in comments_dict[element[9]] %}{% if val.split(':')[0] == 4|string %}"{{ val.split(':')[1] }}",{% endif %}{% endfor %}];
        $("#select_prog_{{ requirements.index(element) }}").empty();
        $.each( prog_comment4, function( index, value ) {
            // this function will add all the values corresponding with the number 4 (worst comments)
            $("#select_prog_{{ requirements.index(element) }}").append('<option>'+value+'</option>');
        });
        break;
    }
});

{% endif %}
{% endfor %}
});
