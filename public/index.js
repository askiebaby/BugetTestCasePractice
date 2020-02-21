import clickcb from './click.js'

window.onload = function(){
    const submitButton = document.querySelector('#submit');
    submitButton.addEventListener('click', clickcb);
}