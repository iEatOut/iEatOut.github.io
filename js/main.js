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
       'email' : $('#ieo-login-email').val(),
       'password' : $('#ieo-login-pass').val()
   }, function(error, authData) {
       if (error) {
           fw.alert(error.message, 'Error');
       } else {
           fw.alert('Login success!', 'Success', function (e) {
               fb.child('profiles/' + fb.getAuth().uid).once('value', function(data) {
                   if (data.val()) {
                       mainView.router.loadPage('main.html');
                   } else {
                       mainView.router.loadPage('health.html');
                   }
               }, function (error) {
                   fw.alert(error.message, 'Error');
               });
           });
       }
   });
});

$$(document).on('pageAfterAnimation', function (e) {
    fw.closeModal('#ieo-login-popup');
});

$('#ieo-register-submit').click(function (e) {
    fb.createUser({
        'email' : $('#ieo-register-email').val(),
        'password' : $('#ieo-register-pass').val()
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

function profileSubmit() {
    var ref = fb.child('profiles/' + fb.getAuth().uid);
    ref.set({
        'name' : $('#ieo-profile-name').val(),
        'gender' : $('#ieo-profile-gender').val(),
        'allergies' : {
            'dairy' : $('#ieo-profile-allergies-dairy').val(),
            'egg' : $('#ieo-profile-allergies-egg').val(),
            'gluten' : $('#ieo-profile-allergies-gluten').val(),
            'peanuts' : $('#ieo-profile-allergies-peanuts').val(),
            'seafood' : $('#ieo-profile-allergies-seafood').val(),
            'sesame' : $('#ieo-profile-allergies-sesame').val(),
            'soy' : $('#ieo-profile-allergies-soy').val(),
            'treenuts' : $('#ieo-profile-allergies-treenuts').val(),
            'wheat' : $('#ieo-profile-allergies-wheat').val()
        },
        'diet' : $('#ieo-profile-diet').val()
    }, function (error) {
        if (error) {
            fw.alert(error.message, 'Error');
        } else {
            fw.alert('Profile successfully recorded!', 'Success', function (e) {
                mainView.router.loadPage('main.html');
            });
        }
    });
}

$('#ieo-profile-submit').click(function (e) { profileSubmit(); });