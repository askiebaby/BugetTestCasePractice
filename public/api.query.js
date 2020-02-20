export default function postQuery (range) {
    return axios.post('/v1/query/', range).then(res=>{
        return res.data
    })
}