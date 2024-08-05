// script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    
    // Example: Alert message on button click
    const button = document.getElementById('my-button');
    if (button) {
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    }
});
