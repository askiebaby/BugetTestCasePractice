export default function postbudge (budge) {
    return axios.post('http://10.1.67.195:5000/v1/budget/', budge).then(res=>{
        return res.data
    })
}