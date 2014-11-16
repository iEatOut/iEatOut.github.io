// Initialize your app
var fw = new Framework7();
var fb = new Firebase('https://sizzling-inferno-727.firebaseio.com');

// Export selectors engine
var $$ = Dom7;

var mainView = fw.addView('#ieo-view', { dynamicNavbar: true });

// Callbacks to run specific code for specific pages, for example for About page:
fw.onPageInit('about', function (page) {
    // run createContentPage func after link was clicked
    $$('.create-page').on('click', function () {
        createContentPage();
    });
});

// Generate dynamic page
var dynamicPageIndex = 0;
function createContentPage() {
	mainView.router.loadContent(
        '<!-- Top Navbar-->' +
        '<div class="navbar">' +
        '  <div class="navbar-inner">' +
        '    <div class="left"><a href="#" class="back link"><i class="icon icon-back"></i><span>Back</span></a></div>' +
        '    <div class="center sliding">Dynamic Page ' + (++dynamicPageIndex) + '</div>' +
        '  </div>' +
        '</div>' +
        '<div class="pages">' +
        '  <!-- Page, data-page contains page name-->' +
        '  <div data-page="dynamic-pages" class="page">' +
        '    <!-- Scrollable page content-->' +
        '    <div class="page-content">' +
        '      <div class="content-block">' +
        '        <div class="content-block-inner">' +
        '          <p>Here is a dynamic page created on ' + new Date() + ' !</p>' +
        '          <p>Go <a href="#" class="back">back</a> or go to <a href="services.html">Services</a>.</p>' +
        '        </div>' +
        '      </div>' +
        '    </div>' +
        '  </div>' +
        '</div>'
    );
	return;
}

function popup(title, text, target) {
    $('#ieo-popover-title').text(title);
    $('#ieo-popover-text').text(text);
    fw.popover('#ieo-popover', target);
}

$('#ieo-login-submit').click(function (e) {
   fb.authWithPassword({
       email    : $('#ieo-login-email').val(),
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

$$(document).on('pageBeforeRemove', function (e) {
    fw.closeModal('#ieo-login-popup');
});

$('#ieo-register-submit').click(function (e) {
    fb.createUser({
        email    : $('#ieo-register-email').val(),
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