const input = document.querySelectorAll('input');
const textArea = document.querySelectorAll('textarea');
const button = document.getElementById('profile-form-buton-js');

for (let i = 0 ; i < input.length; i++) {
    input[i].addEventListener('change', function(e) {
        button.classList.remove("disabled");
    });
    textArea[i].addEventListener('change', function(e) {
        button.classList.remove("disabled");
    });
}