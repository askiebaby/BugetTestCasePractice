const index = require("../index.js");
const click = require("../click")

test("Add a budget", () => {
  document.body.innerHTML =
    "<div>" +
    '  <input id="date" />' +
    '  <input id="amount" />' +
    '  <button id="submit" />' +
    "</div>";

    document.querySelector('#date').value = 202002
    document.querySelector('#amount').value = 20000

    const mockClick = jest.fn(()=>{
        const date = document.querySelector('#date').value
        const amount = document.querySelector('#amount').value

        const obj = {
            date,
            amount
        }
        console.log('submitButton clicked: ',obj);
        return obj  
    });

    const submitButton = document.querySelector('#submit');
    submitButton.addEventListener('click', mockClick);

    submitButton.click();

    expect(mockClick.mock.calls.length).toBe(1);

    
});
