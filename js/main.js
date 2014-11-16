// Initialize your app
var fw = new Framework7();
var fb = new Firebase('https://sizzling-inferno-727.firebaseio.com');

// Export selectors engine
var $$ = Dom7;

var mainView = fw.addView('#ieo-view', { dynamicNavbar: true });

function popup(title, text, target) {
    $('#ieo-popover-title').text(title);
    $('#ieo-popover-text').text(text);
    fw.popover('#ieo-popover', target);
}

$('#ieo-login-submit').click(function (e) {
   fb.authWithPassword({
       email : $('#ieo-login-email').val(),
       password : $('#ieo-login-pass').val()
   }, function(error, authData) {
       if (error) {
           fw.alert(error.message, 'Error');
       } else {
           fw.alert('Login success!', 'Success', function (e) {
               mainView.router.loadPage('health.html');
           });
       }
   });
});

$$(document).on('pageAfterAnimation', function (e) {
    fw.closeModal('#ieo-login-popup');
});

$('#ieo-register-submit').click(function (e) {
    fb.createUser({
        email : $('#ieo-register-email').val(),
        password : $('#ieo-register-pass').val()
    }, function(error) {
        if (error) {
            fw.alert(error.message, 'Error');
        } else {
            fw.alert('Registration success!\nLogin to continue.', 'Success', function (e) {
                fw.closeModal('#ieo-register-popup');
                fw.popup('#ieo-login-popup');
            });
        }
    });
});