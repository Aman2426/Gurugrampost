
console.log('I work!');

var replyButtons = document.getElementsByClassName('reply_button');
var forms = document.getElementsByClassName('reply_form');

for (var i = 0; i < replyButtons.length; i++) {
    replyButtons[i].addEventListener('click', function() {
        var form = this.nextElementSibling;
        if (form.style.display === 'block') {
            form.style.display = 'none';
        } else {
            form.style.display = 'block';
        }
    });
}

document.querySelector('.nav-toggle-button').addEventListener('click', function() {
    // Toggle the 'active' class on the navbar
    document.querySelector('.nav').classList.toggle('active');
  });

  document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('password_change_form');
    var inputs = form.querySelectorAll('input');

    inputs.forEach(function(input) {
        input.classList.add('form-control');
    });
});