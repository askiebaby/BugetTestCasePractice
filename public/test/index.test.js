const index = require("../index.js");
const axios = require("axios");

test("Add a budget", async () => {
  document.body.innerHTML =
    "<div>" +
    '  <input id="date" />' +
    '  <input id="amount" />' +
    '  <button id="submit" />' +
    '  <span id="messageBox" />' +
    "</div>";

  document.querySelector("#date").value = 202002;
  document.querySelector("#amount").value = 20000;

  //
  const mockClick = jest.fn(async () => {
    const date = document.querySelector("#date").value;
    const amount = document.querySelector("#amount").value;
    const messageBox = document.getElementById("messageBox");

    const budge = {
      date,
      amount
    };

    const postbudgeResult = await postbudge(budge);
    messageBox.innerHTML = postbudgeResult.message;
    
    return postbudgeResult;
  });

  function postbudge(budge) {
    return axios.post("http://10.1.67.195:5000/v1/budget/", budge).then(res => {
      return res.data;
    });
  }

  const submitButton = document.querySelector("#submit");
  submitButton.addEventListener("click", async ()=>{
    await mockClick();
  });

  await submitButton.click();

  expect(mockClick.mock.calls.length).toBe(1);
  console.log(mockClick.mock.results[0].value)
});
