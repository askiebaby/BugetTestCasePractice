async function clickcb(){
    const date = document.querySelector('#date').value
    const amount = document.querySelector('#amount').value
    const messageBox = document.getElementById("messageBox")

    const budge = {
        date,
        amount
    }

    const postbudgeResult = await postbudge(budge);
    console.log(messageBox, postbudgeResult);
    messageBox.innerHTML = postbudgeResult.message;


    return postbudgeResult;
}

function postbudge (budge) {
    return axios.post('/v1/budget/', budge).then(res=>{
        return res.data
    })
}