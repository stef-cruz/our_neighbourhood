/*
Enable button "update profile" when change is detected in the input & text area fields
*/

// Selectors
const input = document.querySelectorAll('input');
const textArea = document.querySelectorAll('textarea');
const button = document.getElementById('profile-form-buton-js');

// If user types in the input field, enable button
if (input) {
    for (let i = 0; i < input.length; i++) {
        input[i].addEventListener('change', function (e) {
            button.classList.remove("disabled");
        });
    }
}

// If user types in the textarea field, enable button
if (textArea) {
    for (let j = 0; j < textArea.length; j++) {
        textArea[j].addEventListener('change', function (e) {
            button.classList.remove("disabled");
        });
    }
}

