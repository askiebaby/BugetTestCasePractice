import postQuery from './api.query.js'

export default async function clickQuery(){
    const start_date_v = document.querySelector('#startDate').value
    const end_date_v = document.querySelector('#endDate').value

    const result = document.getElementById("result")

    const start_date = start_date_v.split('-').join('')
    const end_date = end_date_v.split('-').join('')

    if(start_date==="" || end_date==="") return window.alert("please select a date")

    
    const range = {
        start_date,
        end_date
    }

    console.log(range)

    const postQueryResult = await postQuery(range);
    console.log(postQueryResult)
    result.innerHTML = postQueryResult.total_amount;


    // return postbudgeResult;
}