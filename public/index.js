import clickcb from './click.js'
import clickQuery from './query-click.js'

window.onload = function(){
    const submitButton = document.querySelector('#submit');
    submitButton.addEventListener('click', clickcb);

    const queryButton = document.querySelector('#query');
    queryButton.addEventListener('click', clickQuery);
}