// Initialize your app
var fw = new Framework7();
var fb = new Firebase('https://sizzling-inferno-727.firebaseio.com');

// Export selectors engine
var $$ = Dom7;

var mainView = fw.addView('.view-main', { dynamicNavbar: true });

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
                       mainView.router.loadPage('list.html');
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

$$(document).on('pageInit', function (e) {
    var target = $(e.target);
    if (target.data("page") == "health") {
        fb.child('profiles/' + fb.getAuth().uid).once('value', function(data) {
            var info = data.val();

            if (info) {
                $('#ieo-profile-name').val(info["name"]);
                $('#ieo-profile-gender').val(info["gender"]);
                var allergies = info["allergies"];
                $('#ieo-profile-allergies-dairy').prop('checked', allergies["dairy"]);
                $('#ieo-profile-allergies-egg').prop('checked', allergies["egg"]);
                $('#ieo-profile-allergies-gluten').prop('checked', allergies["gluten"]);
                $('#ieo-profile-allergies-peanuts').prop('checked', allergies["peanuts"]);
                $('#ieo-profile-allergies-seafood').prop('checked', allergies["seafood"]);
                $('#ieo-profile-allergies-sesame').prop('checked', allergies["sesame"]);
                $('#ieo-profile-allergies-soy').prop('checked', allergies["soy"]);
                $('#ieo-profile-allergies-treenuts').prop('checked', allergies["treenuts"]);
                $('#ieo-profile-allergies-wheat').prop('checked', allergies["wheat"]);
                $('#ieo-profile-diet').val(info["diet"]);
                $('#ieo-profile-heartdisease').val(info["heartdisease"]);
                $('#ieo-profile-alcoholtobacco').val(info["alcoholtobacco"]);
            }
        }, function (error) {
            fw.alert(error.message, 'Error');
        });
    } else if (target.data("page") == "list") {
        try {
            $.getJSON("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
            lat + "," + long + "&key=AIzaSyATwdAhys3Yde0-OA0vLabSkOqsM4KZJm8", function (data) {
                var results = data["results"];
                for (var i = 0; i < results.length; i++) {
                    if ($.inArray("locality", results[i]["types"])) {
                        if (results[i]["short_name"] != "undefined") {
                            $("#ieo-results-title").text("Results for Near " + results[i]["short_name"]);
                        }
                        break;
                    }
                }
            });
        } catch (err) {

        }
    }
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

function retrieveHealth() {
    mainView.router.loadPage("health.html");
}

function profileSubmit() {
    var ref = fb.child('profiles/' + fb.getAuth().uid);
    ref.set({
        'name' : $('#ieo-profile-name').val(),
        'gender' : $('#ieo-profile-gender').val(),
        'allergies' : {
            'dairy' : $('#ieo-profile-allergies-dairy').is(':checked'),
            'egg' : $('#ieo-profile-allergies-egg').is(':checked'),
            'gluten' : $('#ieo-profile-allergies-gluten').is(':checked'),
            'peanuts' : $('#ieo-profile-allergies-peanuts').is(':checked'),
            'seafood' : $('#ieo-profile-allergies-seafood').is(':checked'),
            'sesame' : $('#ieo-profile-allergies-sesame').is(':checked'),
            'soy' : $('#ieo-profile-allergies-soy').is(':checked'),
            'treenuts' : $('#ieo-profile-allergies-treenuts').is(':checked'),
            'wheat' : $('#ieo-profile-allergies-wheat').is(':checked')
        },
        'diet' : $('#ieo-profile-diet').val(),
        'heartdisease' : $('#ieo-profile-heartdisease').val(),
        'alcoholtobacco' : $('#ieo-profile-alcoholtobacco').val()
    }, function (error) {
        if (error) {
            fw.alert(error.message, 'Error');
        } else {
            fw.alert('Profile successfully recorded!', 'Success', function (e) {
                mainView.router.loadPage('list.html');
            });
        }
    });
}

$('#ieo-profile-submit').click(function (e) { profileSubmit(); });

var page;

function mainClick(ele) {
    page = $(ele).children('.item-title').text();
    mainView.router.loadPage('list.html');
}

function back() {
    mainView.router.back();
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        fw.alert('Location not available for this browser!', 'Error');
    }
}

var lat;
var long;

function showPosition(position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
}