$(function() {

    $("input,textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            // get values from FORM
            var name = $("input#name").val();
            var email = $("input#email").val();
            var phone = $("input#phone").val();
            var message = $("textarea#message").val();
            var firstName = name; // For Success/Failure Message
            // Check for white space in name for Success/Fail message
            if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }
            var mailtoURI = "mailto:contact@awesomebarnes.com?subject=" + encodeURI("Contact form message from " + name);
            mailtoURI += "&body=";
            mailtoURI += encodeURI("Name:\t" + name + "\n");
            mailtoURI += encodeURI("Email:\t" + email + "\n");
            if(phone) {
              mailtoURI += encodeURI("Phone:\t" + phone + "\n");
            }
            mailtoURI += encodeURI("\n" + message);
            window.open(mailtoURI);
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});
