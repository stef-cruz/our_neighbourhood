/*
Enable button "update profile" when change is detected in the input & text area fields
*/

// Selectors
const input = document.querySelectorAll('input');
const textArea = document.querySelectorAll('textarea');
const button = document.getElementById('profile-form-buton-js');

// If user types in the input field, enable button
for (let i = 0 ; i < input.length; i++) {
    input[i].addEventListener('change', function(e) {
        button.classList.remove("disabled");
    });
}

// If user types in the textarea field, enable button
for (let j = 0 ; j < input.length; j++) {
    textArea[j].addEventListener('change', function(e) {
        button.classList.remove("disabled");
    });
}