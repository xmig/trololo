function set_kind(value) {
    document.forms['login_form'].elements["kind"].value = value;
    document.forms['login_form'].submit();
}
//================================================================

$(document).ready(function(){

var wrong = $('i.validPass'),
    passLogin = $('#nucPass'),
    valid = $('div.validPass'),
    confirmLogin = $('#nucConfirm');

    function checkYesNo() {
    var pass = passLogin.val();
    var confirm = confirmLogin.val();

        if (pass == confirm && confirm != '' && pass != '') {
            valid.removeClass('has-error').addClass('has-success');
            wrong.removeClass('glyphicon-lock').addClass('glyphicon-ok');
        } else {
            valid.removeClass('has-success').addClass('has-error');
            wrong.removeClass('glyphicon-ok').addClass('glyphicon-lock');
        }
    }

    passLogin.on('input', checkYesNo);
    confirmLogin.on('input', checkYesNo);
});